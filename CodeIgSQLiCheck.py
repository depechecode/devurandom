#!/usr/bin/python

import os

def recurfind(p,text,level):
        for item in os.listdir(p):
                if os.path.isdir(os.path.join(p,item)):
                        newlevel = level + "--"
                        print newlevel + item + "(d)"
                        newpath = os.path.join(p,item)
                        recurfind(newpath,text,newlevel)
                elif os.path.isfile(os.path.join(p,item)):
                       flag = 0
                       newlevel = level + "--"
                       newpath = os.path.join(p,item)
                       file = open(newpath,"r")
                       for line in file.readlines():
                            if text in line:
                                   flag = 1
                                   break
                       if (flag == 1):
                            print newpath + ": String found!"
                            file.seek(0)
                            for line in file.readlines():
                                    if text in line:
                                           print line + "Manually Check Code for CI SQLi Issues"

                    
                       file.close()

path = raw_input("Please enter the directory to recursively search in: ")
#text = raw_input("Please enter the string to look for in the file contents: ")
text = "is_numeric"
recurfind(path,text,"")