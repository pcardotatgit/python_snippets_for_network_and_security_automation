#!usr/bin/env python
# -*- coding: UTF-8 -*-
# https://docs.python.org/2/library/argparse.htm
import os
import sys
from crayons import *
      
def main(dir):
    if not os.path.isdir(dir):
        print ('diretory doesn t exists in the current directory')
        return
    else:
        print ('OK the directory exists this is :')
        print (yellow(dir,bold=True))
        count = 0
        for root, dirs, files in os.walk(dir):        
            print( len(files), "this one is a non-directory files")
            for name in files:    
                print(cyan(dir+'/'+name))    
                if name.find('.csv') >=0:
                    print(green('    >>>> Ok let s take this one',bold=True))
                    file_path = os.path.join(root, name)
                    print(cyan(file_path)) 

if __name__ == '__main__':
    dir = os.getcwd()
    print(dir)
    main(dir)