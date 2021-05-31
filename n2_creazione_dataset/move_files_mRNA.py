import os
import shutil


final_file_path = os.getcwd()
mRNApath = os.getcwd()
mRNApath = os.path.join(mRNApath, os.pardir) + "\mRNA"

for root, dirs, files in os.walk(mRNApath, topdown=False):
    ciao = 1
if len(dirs) == 0:
    print('no dir')
    exit(1)

path = mRNApath
for d in dirs:
    path = mRNApath + '\\' + d
    # print(path)
    files = os.listdir(path)
    # print(files)
    for f in files:
        if ('annotation' not in f) & ('log' not in f):
            src = path+'\\'+f
            dst = mRNApath+'\\'+f
            shutil.move(src, dst)
    shutil.rmtree(path)

print('end moving')
