import os
import shutil
from os import path
import sys
import syslog
import fileinput


def main():
    if path.exists("pamso.txt"):
        nav = path.realpath("pamso.txt"); 
if __name__ == "__main__":                 
    main()

set_vs = 0
try:
    f = open("//etc/pam.d/sudo","r")
    data_k = ("auth       sufficient     pam_tid.so\n")
    odata = f.readlines()
    odata.insert(1,data_k)
    f.close()
    set_vs += 1
finally:
    f = open("//etc/pam.d/sudo","w")
    f.writelines(odata)
    f.close()
    set_vs += 1

#Debug Program
if(set_vs == 0):
    print("File execution Issue\, Please report in github issues page")
elif(set_vs == 1):
    print("Write error, Please report in Github issues Page")
elif(set_vs==2):
    print("Success")
else:
    print("Unidentified error, Please report in Github issues Page")
