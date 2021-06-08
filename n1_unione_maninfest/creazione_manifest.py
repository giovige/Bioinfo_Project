# apro il file json e collego il case_id al file_name tramite una dict.
mrnaJson = '2_mRNA.json'
mrnaManifest = '2_mRNA_manifest.txt'
mirnaJson = '1_miRNA.json'
mirnaManifest = '1_miRNA_manifest.txt'

f_m_j = open(mrnaJson, 'r')

list_m = {}  # case_id : file_name
label_m = {}  # file_name : project_id
line_m = f_m_j.readline()
while line_m:
    if "case_id" in line_m:  # id paziente
        caseid = line_m.split(' ')
        caseid = caseid[7].split('"')
        caseid = caseid[1]

    if "project_id" in line_m:  # tipo di tumore
        lb = line_m.split(' ')
        lb = lb[9].split('"')
        lb = lb[1]

    if "file_name" in line_m:
        filename = line_m.split(' ')
        filename = filename[3].split('"')
        filename = filename[1]

        list_m[filename] = []  # dict con (filename,case_id)
        list_m[filename].append(caseid)

        label_m[filename] = []      # dict con (filename, label tumore)
        label_m[filename].append(lb)

    line_m = f_m_j.readline()
f_m_j.close()

# apro il file json e collego il case_id al file_name tramite una dict.
f_mi_j = open(mirnaJson, 'r')
line_mi = f_mi_j.readline()
label_mi = {}
list_mi = {}
while line_mi:
    if "case_id" in line_mi:
        caseid = line_mi.split(' ')
        caseid = caseid[7].split('"')
        caseid = caseid[1]

    if "project_id" in line_mi:
        lb = line_mi.split(' ')
        lb = lb[9].split('"')
        lb = lb[1]

    if "file_name" in line_mi:
        filename = line_mi.split(' ')
        filename = filename[3].split('"')
        filename = filename[1]

        label_mi[filename] = []     # dict con (filename, label tumore)
        label_mi[filename].append(lb)

        list_mi[filename] = []      # dict con (filename,case_id)
        list_mi[filename].append(caseid)
    line_mi = f_mi_j.readline()
f_mi_j.close()

man_m = []  # lista di filename:caseId senza doppioni e pazienti presenti in entrambi i file json (per mRNA)
man_mi = []  # lista di filename:caseId senza doppioni e pazienti presenti in entrambi i file json (per miRNA)
for k in list(list_m.values()):
    if k in list(list_mi.values()):
        man_m.append(list(list_m.keys())[list(list_m.values()).index(k)])  # get keys from value
        man_mi.append(list(list_mi.keys())[list(list_mi.values()).index(k)])

# Rimuovo doppioni
man_m = list(dict.fromkeys(man_m))
man_mi = list(dict.fromkeys(man_mi))

new_label_m = {}
for file in man_m:
    if file in label_m:
        new_label_m[file] = []
        new_label_m[file].append(label_m[file])

new_label_mi = {}
for file in man_mi:
    if file in label_mi:
        new_label_mi[file] = []
        new_label_mi[file].append(label_mi[file])

# Creo il file ciao che sarò il mio nuovo manifest con soltanto i soggetti in comune
f_m_m = open(mrnaManifest, 'r')
unionManifest_m = []
line_m = f_m_m.readlines()
unionManifest_m.append(line_m[0])
for line in man_m:
    for riga in line_m:
        riga1 = riga.split('\t')
        if riga1[1] == line:
            unionManifest_m.append(riga)
f_m_m.close()

# #Creo il file unionManifest che sarò il mio nuovo manifest con soltanto i soggetti in comune
f_m_m = open(mirnaManifest, 'r')
unionManifest_mi = []
line_m = f_m_m.readlines()
unionManifest_mi.append(line_m[0])
for line in man_mi:
    for riga in line_m:
        riga1 = riga.split('\t')
        if riga1[1] == line:
            unionManifest_mi.append(riga)
f_m_m.close()

# Salvataggi
# Manifest mRNA
f = open('nuovo_manifest_m.txt', 'w+')
for line in unionManifest_m:
    f.write(line)
f.close()
# #Manifest miRNA
f = open('nuovo_manifest_mi.txt', 'w+')
for line in unionManifest_mi:
    f.write(line)
f.close()
# Label miRNA
g = open('new_label_mi.txt', 'w+')
for l in list(new_label_mi.keys()):
    g.write(f'{l}:{new_label_mi[l]} \n')
g.close()
# Label mRNA
g = open('new_label_m.txt', 'w+')
for l in list(new_label_m):
    g.write(f'{l}:{new_label_m[l]} \n')
g.close()
