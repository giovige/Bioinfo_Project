import os
import shutil


final_file_path = os.getcwd()
miRNApath = os.getcwd()
miRNApath = os.path.join(miRNApath, os.pardir) + "\miRNA"

for root, dirs, files in os.walk(miRNApath, topdown=False):
    ciao = 1

if len(dirs) == 0:
    print('no dir')
    exit(1)

path = miRNApath
moveto = miRNApath
for d in dirs:
    path = miRNApath + '\\' + d
    # print(path)
    files = os.listdir(path)
    # print(files)
    for f in files:
        if ('annotation' not in f) & ('log' not in f):
            src = path+'\\'+f
            dst = miRNApath+'\\'+f
            shutil.move(src, dst)
    shutil.rmtree(path)

print('end moving')
