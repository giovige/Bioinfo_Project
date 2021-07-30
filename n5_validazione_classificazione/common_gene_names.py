import webbrowser
import time
import pandas as pd
import numpy as np
import requests
from sys import argv


# Function 'common_genes_names' traslates the genes names to the ENSEMBL Gene ID to the common names.
# If the common name related to the ENSEMBL Gene ID is not found, the function will recopy the ENSEMBL Gene ID.
def common_genes_names(name_list):
    # Traslate to common name notation
    common_names = []
    for gene in name_list:
        gl = gene.split('.')
        server = "https://rest.ensembl.org"
        ext = f"/overlap/id/{gl[0]}?feature=gene"
        r = requests.get(server + ext, headers={"Content-Type":
                                                    "application/json"})
        if '#' in gene:
            fout.write('\n' + gene + '\n')
            pass

        if not r.ok:
            # r.raise_for_status()
            # sys.exit()
            common_names.append(f'{gl[0]}')

        # print(decoded)
        else:
            decoded = r.json()
            for element in decoded:
                id = element['gene_id']
                if id == gl[0]:
                    if 'external_name' in element:
                        common_names.append(element['external_name'])
                        fout.write(element['external_name'] + '  -->  ' + element['external_name'] + ' \n')
                        time.sleep(10)  # Sleep for 3 seconds
                        webbrowser.open('https://www.proteinatlas.org/' + gl[0] + '-' + element['external_name'] + '/pathology/renal+cancer') #open the web pages for interested gene
                    else:
                        common_names.append(f'{gl[0]}')
                        fout.write(gl[0] + '\n')

    return common_names


# Import data
name, file = argv
fin = open(file, 'r')
names = fin.readlines()
fin.close()
file = str(file).split('.')[0] + '_common.txt'
fout = open(file, 'w+')
fout.write(file + '\n\n')
common_genes_names(names)
fout.close()
print('fine')
