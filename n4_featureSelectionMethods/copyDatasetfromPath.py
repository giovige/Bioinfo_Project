import os
import shutil
from os.path import isfile

target_path = os.getcwd()
source_path = input('> Source folder name where CSV files are in (write "." for the project root folder) = ')
source_path = os.path.join(target_path, os.pardir) + "\\" + source_path

toMove = []
files = [f for f in os.listdir(source_path) if isfile(os.path.join(source_path, f))]
for file in files:
    if file.endswith(".csv"):
        toMove.append(file)

if len(toMove) > 0:
    print(toMove)
else:
    print("No dataset file to move!")
    exit(-3)

for f in toMove:
    src = source_path + '\\' + f
    dst = target_path + '\\' + f
    shutil.move(src, dst)

print('end moving')
