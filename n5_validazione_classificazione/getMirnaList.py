from sys import argv


def getMirnaList(file):
    features = []
    # filename = 'mirna_best.txt'
    f = open(filename, 'r')
    line = f.readline()
    while line:
        line = line.strip('\n')
        features.append(line)
        line = f.readline()
    # print(features)


scriptname, filename = argv
getMirnaList(filename)

