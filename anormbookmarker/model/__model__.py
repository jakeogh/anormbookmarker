#!/usr/bin/env python3

## https://stackoverflow.com/questions/1057431/how-to-load-all-modules-in-a-folder

print("anormbookmarker.model.__init__.py")
import os
module_path = os.path.dirname(__file__)
for module in os.listdir(module_path):
    if module == '__init__.py' or module[-3:] != '.py' or not module[0].isupper():
        continue
    classname = module[:-3]
    globals()[classname] = __import__('anormbookmarker.model.'+classname, globals=globals(), locals=locals(), fromlist=[classname], level=0)

    cmd_to_eval = classname + ' = ' + classname + '.' + classname
    #import IPython; IPython.embed()
    #print(cmd_to_eval)
    exec(cmd_to_eval) #sshhhhhhhh
del module
del classname
del cmd_to_eval
