import os
path="f:/dwg/"
filename="迁改"
for root,dirs,files in os.walk(path):
    for name in files:
        if filename in name :
           print(os.path.join(root,name))
    for name in dirs:
        print(os.path.join(root,name))
        
