import os
import sys
def check_dir(name):
    ndir = 0
    nf = 0
    lst_ = os.listdir(path=name)
    for i in lst_:
        new_name = name+'/'+i
        if os.path.isdir(new_name): 
            ndir += 1
            a, b = check_dir(new_name)
            nf = nf + a 
            ndir = ndir + b
        else: nf += 1
    return nf, ndir

name = sys.stdin.read()
print(*check_dir(name))
