import pandas as pd
import numpy as np
import re
from xgboost import XGBRegressor
import math
#############################STORE-HOUSE$##############################
train=pd.read_csv(r'C:\Users\TARUN\Desktop\New folder (3)\Book_price_prediction\Participants_Data\Train1.csv')
#np.sqrt(np.square(np.log10(y_pred +1) - np.log10(y_true +1)).mean())
train['new_1']=train['Reviews']//train['Ratings']
test=pd.read_csv(r'C:\Users\TARUN\Desktop\New folder (3)\Book_price_prediction\Participants_Data\Test.csv')

pattern=r'[A-Za-z]+'
title=[]
len_title=[]
for i in train['Title'].unique():
    title.append(i)
for i in range(0,len(title)):
    len_title.append(i)

for i,j in zip(title,len_title):
    test['Title']=test['Title'].replace(i,j)

tit=[]
len_tit=[]
for i in test['Title'].unique():
    if(re.search(pattern,str(i))):
        tit.append(i)

for i in range(len(title),len(title)+len(tit)):
    len_tit.append(i)


for i,j in zip(tit,len_tit):
    test['Title']=test['Title'].replace(i,j)
test['Title']=test['Title'].replace('11.22.63',len(title)+len(tit)+1)

test['Title']=test['Title'].astype(float)

#########################################


author=[]
len_author=[]
for i in train['Author'].unique():
    author.append(i)
for i in range(0,len(author)):
    len_author.append(i)
for i,j in zip(author,len_author):
    test['Author']=test['Author'].replace(i,j)

writer=[]
len_writer=[]

for i in test['Author'].unique():
    if(re.search(pattern,str(i))):
        writer.append(i)
for i in range(len(author),len(author)+len(writer)):
    len_writer.append(i)

for i,j in zip(writer,len_writer):
    test['Author']=test['Author'].replace(i,j)

edition=[]
len_edition=[]

for i in (train['Edition'].unique()):
    edition.append(i)

for i in range(0,len(edition)):
    len_edition.append(i)

for i, j in zip(edition,len_edition):
    test['Edition']=test['Edition'].replace(i,j)
e=[]
len_e=[]

for i in (test['Edition'].unique()):
    if(re.search(pattern,str(i))):
        e.append(i)

for i in range(len(edition),len(edition)+len(e)):
    len_e.append(i)

for i, j in zip(e,len_e):
    test['Edition']=test['Edition'].replace(i,j)
######################################################
for  i in (test['Reviews'].unique()):
    test['Reviews'] = test['Reviews'].replace(i,str(i).split(' ')[0])
######################################################
for  i in (test['Ratings'].unique()):
    test['Ratings'] = test['Ratings'].replace(i,str(i).split(' ')[0])

pattern2=r'\,'
for  i in (test['Ratings'].unique()):
    if(re.search(pattern2,str(i))):
        test['Ratings'] = test['Ratings'].replace(i,re.sub(pattern2,'',i))


####################################################
genre=[]
len_genre=[]
for i in train['Genre'].unique():
    genre.append(i)

for i in range(0,len(genre)):
    len_genre.append(i)

for i,j in zip(genre,len_genre):
    test['Genre']=test['Genre'].replace(i,j)

g=[]
len_g=[]
for i in test['Genre'].unique():
    if(re.search(pattern,str(i))):
        g.append(i)

for i in range(len(genre),len(genre)+len(g)):
    len_g.append(i)

for i,j in zip(g,len_g):
    test['Genre']=test['Genre'].replace(i,j)



##################################################
category=[]
len_category=[]
for i in train['BookCategory'].unique():
    category.append(i)
for i in range(0,len(category)):
    len_category.append(i)
for i,j in zip(category,len_category):
    test['BookCategory']=test['BookCategory'].replace(i,j)

















































