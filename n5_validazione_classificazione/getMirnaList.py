from sys import argv


def getMirnaList(file):     # legge file con miRNA presi dalla letteratura
    features = []
    f = open(file, 'r')
    line = f.readline()
    while line:
        line = line.rstrip()
        features.append(line)
        line = f.readline()
    # print(features)
    f.close()
    return features


scriptname, filenameIN, filenameOUT = argv
cnt = 0
foutname = 'res_' + str(filenameOUT).split('.')[0] + '.txt'
# fp = open('res50_MI_unsupervised.txt', 'a+')
fp = open(foutname, 'a+')
fp.write('\n')
ftIN = getMirnaList(filenameIN)
ftOUT = getMirnaList(filenameOUT)
for f in ftOUT:
    if f in ftIN:
        cnt += 1
        fp.write(str(f) + '\n')
        print(f)
print(filenameOUT + ' contains ' + str(cnt) + '/' + str(len(ftOUT)) + '  using the file ' + filenameIN)
fp.write(filenameOUT + ' contains ' + str(cnt) + '/' + str(len(ftOUT)) + '  using the file ' + filenameIN)
fp.write('\n')
fp.close()
