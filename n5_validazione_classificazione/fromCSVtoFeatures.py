from sys import argv
import pandas as pd
import numpy as np


name, file = argv
m_data = pd.read_csv(str(file), index_col=[0])
names_m_ft = np.array(m_data.axes[1])
foutnameM = str(file).split('.')[0] + '_20_mRNA.txt'
foutnameMI = str(file).split('.')[0] + '_20_miRNA.txt'
foutM = open(foutnameM, 'w+')
foutMI = open(foutnameMI, 'w+')
# print(len(names_m_ft))
totMI = 0
totM = 0
i = 0
while i < 100:
    if i < 20:
        foutM.write(names_m_ft[i] + '\n')
        totM += 1
    else:
        foutMI.write(names_m_ft[i] + '\n')
        totMI += 1
    i += 1
    if i == 20:  # first 20 mrna
        i = 50
    if i == 70:  # first 20 mirna
        i = 100

# i = 50
# while i < 100:
#     foutMI.write(names_m_ft[i] + '\n')
#     tot += 1
#     i += 1
print(totM)
print(totMI)
foutM.close()
foutMI.close()
