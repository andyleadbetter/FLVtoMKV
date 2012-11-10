'''
Created on Nov 10, 2012

@author: andy
'''
import sys
import os

if __name__ == '__main__':



    def findFlashVideos():
        files_toprocess = set()
        paths = sys.argv[1:]
        for p in paths:
            if os.path.isfile(p) and p.endswith('.flv'):
                files_toprocess.add(p)
            elif os.path.isdir(p):
                for root, dirs, files in os.walk(p):
                    files_toprocess.update([os.path.join(root, f) 
                                            for f in files if f.endswith('.flv')])
        
       