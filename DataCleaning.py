import pandas as pd
import numpy as np
import matplotlib as plt
import seaborn as sns
import statsmodels.api as sm
import re
from Grabber import *


# Portion To Read Four *.csv Dataset Files After Cleaning (Folder Name  "ProjectFiles" )

enrol = pd.read_csv('ProjectFiles/enrol.csv').astype(float, errors='ignore')

clas = pd.read_csv('ProjectFiles/clas.csv').astype(float, errors='ignore')

sex = pd.read_csv('ProjectFiles/sex.csv', index_col=0).astype(float, errors='ignore')

qoe = pd.read_csv('ProjectFiles/qoe.csv').astype(float, errors='ignore')



# Croping Data of "enrol.csv" To Year "2006-2021"
enrol = enrol[(enrol['Academic Year'] >= '2006/07') & (enrol['Academic Year'] <= '2021/22')]

# Removing "Postgraduate & Total From Datset"
enrol = enrol.drop(['Postgraduate', 'Total'], axis=1)

#Merging it With "clas.csv" Dataset File Which Already Has Croped Data Which i Previously Done With "enrol.csv" 
merged_data = pd.merge(enrol, clas, on='Academic Year')

# Saving it As A New File in "NewFiles" Folder Without Manipulating The Previous *.csv Files
merged_data.to_csv('NewFiles/clasenrol.csv', index=False)

#Cleaning "sex.csv" Dataset & Keeping Only These Classes Mentioned in desired_labels
def keep_row(label):
    desired_labels = [
        'Sex',
        'Female',
        'Male',
        'Other',
        'Age group',
        '20 and under',
        '21-24 years',
        '25-29 years',
        '30 years and over',
        'Disability status',
        'Known disability',
        'No known disability'
    ]
    return label in desired_labels

filtered_df = sex[sex.index.to_series().apply(keep_row)]

#Now Saving "sex.csv" Dataset in NewFiles Folder With Same Name Without Disturbing The Original "sex.csv" File
output_file = 'NewFiles/sex.csv'
filtered_df.to_csv(output_file)


#This Function Called From Custom Created Lib What Basically it is Doing:
# 1. Using URL TO Extrat Fee Structure And it Extracted 4 Fee Structures From The Url [xx,xx,xx,xx] Using a Regular Express (Regx)
# 2. Then Created a Custom Range [2000/01 --- 2021/22] And Assigned The Fee Structure Using Ranges Extracted Previously
# 3. Created And Saved a "tf.scv" File And Returned The tf object Here 

tf = Graber_For_Fee()

#Reading "enrol.cv" File To Merge With tf Object !
enrol = pd.read_csv('ProjectFiles/enrol.csv')

#Merged tf and enrol Objects And Saved As New File Named "enroltf.csv"
merged_data = pd.merge(enrol, tf, on='Academic Year')
merged_data.to_csv('NewFiles/enroltf.csv', index=False)

clasenrol = pd.read_csv('NewFiles/clasenrol.csv').astype(float, errors='ignore')
enroltf = pd.read_csv('NewFiles/enroltf.csv').astype(float, errors='ignore')
sex = pd.read_csv('NewFiles/sex.csv').astype(float, errors='ignore')
#Except Fee Data, Logically No Other Data Can Be Converted Into Floats (Person Count Etc)
print(clasenrol)
print(enroltf)
print(sex)






