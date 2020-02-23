import os,time
import os.path
# This folder is custom
rootdir = '.'
for parent, dirnames, filenames in os.walk(rootdir):
    # Case1: traversal the directories
    for dirname in dirnames:
      #  print("Parent folder:", parent)
      #  print("Dirname:", dirname)
         print(parent,dirname)
    # Case2: traversal the files
    for filename in filenames:
       # print("Parent folder:", parent)
       # print("Filename:", filename)
        print(parent,filename)
        # time.sleep(0.1)
