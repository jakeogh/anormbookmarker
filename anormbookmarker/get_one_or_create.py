#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# MIT License

from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import IntegrityError

def get_one_or_create(session, model, *args, create_method='', create_method_kwargs=None, **kwargs):
    '''Find and return existing ORM object or create and return a new one. Adapted from examples.'''
    assert session
    for key in kwargs.keys():
        try:
            if issubclass(kwargs[key].__class__, model):
                return kwargs[key]
        except Exception as e:
            print("Exception:", e)
            quit(1)
    try:
        result = session.query(model).filter_by(**kwargs).one()
    except NoResultFound as e:
        kwargs.update(create_method_kwargs or {})
        created = getattr(model, create_method, model)(*args, **kwargs)
        try:
            session.add(created)
            session.flush(objects=[created])
            return created
        except IntegrityError as e:
            print("IntegrityError:", e, model,
                   "calling getattr() model:", model,
                   "create_method:", create_method,
                   "kwargs:", [str(kwargs)])
            print(model, "calling session.rollback()")
            session.rollback()
            result = session.query(model).filter_by(**kwargs).one()
            print("IntegrityError: got result:", result)
            return result
    return result

