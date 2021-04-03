# coding=utf-8
from sys import argv
import json

def saveOccurences(path, flag):
	id = ''
	fname = ''	
	with open(path) as f:
		line = f.readline()
		while line:
			if "case_id" in line:
				id = line.split(' ')[7].split('"')[1]
			if "file_name" in line:
				fname = line.split(' ')[3].split('"')[1]

				# se ho una coppia non nulla di (id-fname) allora la aggiungo al dizionario
				if  id!='' and fname!='':
					# se id non è ancora presente, lo aggiungo con un value nullo
					if id not in occ.keys():
						occ[id] = []		
					occ[id].append(fname)		# altrimenti aggiungo (appendo) solo il valore di fname
					id = ''
					fname = ''
			line = f.readline()
		f.close()


	if flag == 1:	# vuol dire che sto lavorando sul secondo file: tolgo occorrenze singole 
					#e mantengo quelle in cui ho almeno un file di mrna e uno di mirna
		#print("Deleting...")
		
		with open("deleted.txt", 'w') as deleted:
			for key in list(occ.keys()):
				if len(occ[key]) < 2:
					deleted.write(str(key) + '\n')
					deleted.write('\t\t' + ' --> '+ str(occ[key]) + '\n')
					occ.pop(key)
		deleted.close()

		with open("dump.txt", 'w') as dump:
			n=0
			for k in occ.keys():
				dump.write(str(k) + '\t(' + str( len(occ[k]) ) + ')' +'\n')
				for v in occ[k]:
					n=n+1
					dump.write('\t\t' + ' --> '+ str(v) + '\n')
			dump.write('totale chiavi :' + str(len(occ)) + '\n' )
			dump.write('totale file :' + str(n) + '\n' )
			dump.write('\n\n\n')
			
		dump.close()



def getManifestRecord(path):
	with open(path,'r') as f:
		#manifestList = []
		manifestLines = f.readlines()
		if manifestLines[0] not in manifestList:
			manifestList.append(manifestLines[0])

		kidneyFiles=[]
		for k in occ.keys():
			for v in occ[k]:
				kidneyFiles.append(v)
		
		#per ogni riga del file manifest cerco quelle che hanno come filename 
		#una corrispondenza con i values del dizionario
		for l in manifestLines:
			record = l.split('\t')
			if record[1] in kidneyFiles:
				manifestList.append(l)
		f.close()


print("Main()")
scriptname, json1, json2, manifest1, manifest2 = argv
occ = {}
manifestList = []
saveOccurences(json1, 0)
saveOccurences(json2, 1)

# stampo primi record del dizionario
# i=0
# for key in occ:
# 	print(key,  "--->" , occ[key])
# 	i = i + 1
# 	if i > 3:
# 		break


getManifestRecord(manifest1)
getManifestRecord(manifest2)

#print(manifestList)
#Scrivo il nuovo manifest
fout = open('kidney_manifest.txt','w+')
for line in manifestList:
    fout.write(line)
fout.close()