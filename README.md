# Bioinfo_Project


1) Script#1

- Aggiungere i seguenti parametri per eseguire lo script di creazione del manifest per il download dei dati:

<path_assoluto_cartella_progetto>/unione_maninfest/1_miRNA.json
<path_assoluto_cartella_progetto>/unione_maninfest/2_mRNA.json
<path_assoluto_cartella_progetto>/unione_maninfest/1_miRNA_manifest.txt
<path_assoluto_cartella_progetto>/unione_maninfest/2_mRNA_manifest.txt

- Mettere come working directory la cartella 'unione_maninfest'.

- Avviare script.






2) gdc_client.ee

C:\Users\Giovanni\Desktop\Bio_Project>gdc-client.exe download -m unione_maninfest\nuovo_manifest_m.txt --dir .\mRNA\

C:\Users\Giovanni\Desktop\Bio_Project>gdc-client.exe download -m unione_maninfest\nuovo_manifest_mi.txt --dir .\miRNA\

verificare la conferma di ''Successfully downloaded: 1160''


3) 
move_files_miRNA.py
move_files_mRNA.py

4)
- spostare file LABEL nella cartella creazione_dataset 
- create_dataset_mi.py
- create_dataset_m.py


5)
preprocessing


6)