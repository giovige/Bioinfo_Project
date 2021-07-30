# Bioinfo_Project User Manual 


## Download and pre-processing 
```
The first part of the project is used to download the files of those affected by kidney cancer who have both mRNA and miRNA data. Then the matrices are created with the genes (features) on the columns and the subject's tumor type (labels) on the lines. Finally, the insignificant features are removed and the 'zero-mean' and 'min-max' rescale is done. 

creazione_manifest.py 
This script is responsible for processing the json and manifest files related to mRNA and miRNA, in order to produce the final manifest files that are used to download the data from the server. 
The following global variables are used: pay attention to the names of the files used in the script and present in the folder. 
mrnaJson = '2_mRNA.json' 
mrnaManifest = '2_mRNA_manifest.txt' 
mirnaJson = '1_miRNA.json' 
mirnaManifest = '1_miRNA_manifest.txt' 

2. Data download using the client gdc_client.exe 
With the following commands (run as administrator) the files contained in new_manifest_m.txt and new_manifest_mi.txt are downloaded. 
gdc-client.exe download -m <absolute_path_to_project_folder>\n1_unione_maninfest\nuovo_manifest_m.txt --dir .\mRNA\ 
gdc-client.exe download -m <absolute_path_to_project_folder>\n1_unione_maninfest\nuovo_manifest_mi.txt --dir .\miRNA\ 

N.B.: Check the confirmation message of "Successfully downloaded: 1160". 

3. Dataset creation 

Move the files "new_label_mi.txt" and "new_label_m.txt" (which contain the labels) created in step(1) to the folder ./n2_creazione_dataset.

Run scripts "move_files_miRNA.py" and "move_files_mRNA.py". 
Run script "creazione_dataset.py". 


4. Dataset preprocessing 
Run the script dataset_Preprocessing.py twice, changing from time to time the parameter (the dataset filename) given to the script. 
Input commands: 
dataset_Preprocessing.py dataset_miRNA.csv 
dataset_Preprocessing.py dataset_mRNA.csv 
```


## Feature Selection Methods
```
Two different approaches have been chosen for the data features selection. 
1. Classic: where the FS is carried out on each dataset 
2. multi-view: where the FS is carried out considering the two datasets together. 

For the first approach, the methods considered most suitable in the literature for this type of data were chosen: 
Random Forest mean decrease impurity 
Decision tree 
Xgboost 
KNeighborsRegressor 
RFECV 

Given the high computational cost, the latter two methods are not recommended for mRNA data. 
For the second approach, a method based on the canonical correlation analysis (CCA) was implemented. 

1. copyDatasetfromPath.py 
Every time you need to move multiple dataset files into the n4_featureSelectionMethods folder in order to use them for feature selection methods, run copyDatasetfromPath.py to move every ".csv" file from the source path given as input to the function. 

2. Running FS methods 
Run the script related to the desired FS method and answer the questions asked on the command line: the answers given by the user perform the method with different parameters. 

a) Reduced = implements the FS on the dataset containing a smaller number of labels without considering all subcategories of tumors. Complete = implements the FS on the dataset containing all types of labels.
b) Name of the dataset to use. 
c) Y = saves a dataset that contains only the most relevant features obtained from the FS method used. 
N = executes the FS method without saving the dataset. 


d) Number of features to select (1-1000). 



3. Canonical Correlation Analysis 
To implement a multi-view features selection, a CCA based method is implemented. After selecting the two datasets and the number of features to extract it can be possible to choose between the unsupervised and supervised version of the function. The output will be a new dataset with the top features selected from each input dataset. 
```


## Classification and validation
```
Finally, to demonstrate the quality of the features found, a classifier and validation based on literature data was performed. 

1. Convolutional Neural Network 
In order to evaluate the goodness of the feature selection method a CNN is used for the classification of the data. In particular in "CNN" script is present: 
'Myplot' class for the plot of the confusion matrix. 
'Define the model' in which the CNN is defined. 
'Import Data' where the dataset is divided in train and test set 
'Classification' for the train of the CNN, classification of test set and plot the confusion matrix 



2. Validation 
A method to evaluate the goodness of the features selection is to check in literature if the mRNA and miRNA selected are involved in the renal cancer. As regards the mRNA genes, the "Atlas of human proteins" (https://www.proteinatlas.org/) was used to verify if they were prognostic. For miRNAs, on the other hand, not having found a dataset that provided the desired information, a literature search was done to find studies that demonstrated the involvement of some miRNAs in kidney cancer[1-7]. 

In order to validate features, three scripts are used: 
a) fromCSVtoFeatures.py: gets as input the dataset filename (.csv) and returns two output files, <orignal_dataset_name>_20_mRNA.txt and <orignal_dataset_name>_20_miRNA.txt, each of which contains the list of the top 20 features of mRNA/miRNA. 
b) getMirnaList.py: gets as input two files: 
- text file with the best miRNA features found through a literature search. 
- <orignal_dataset_name>_20_miRNA.txt created at point (a). 
c) common_gene_names.py: gets as input the <orignal_dataset_name>_20_mRNA.txt file. As output returns a file with the gene names translated, and opens a tab in the browser for each gene to verify in proteinatlas.org website.
```
