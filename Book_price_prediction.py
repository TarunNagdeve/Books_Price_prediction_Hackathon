edition=[]
len_edition=[]
import pandas as pd
import numpy as np
import re
from xgboost import XGBRegressor
train=pd.read_csv(r'C:\Users\TARUN\Desktop\New folder (3)\Book_price_prediction\Participants_Data\Train1.csv')
for i in (train['Edition'].unique()):
    edition.append(i)

for i in range(0,len(edition)):
    len_edition.append(i)

for i, j in zip(edition,len_edition):
    train['Edition']=train['Edition'].replace(i,j)
##################################################################
for  i in (train['Reviews'].unique()):
    train['Reviews'] = train['Reviews'].replace(i,str(i).split(' ')[0])

train['Reviews']=train['Reviews'].astype(float)

##################################################################

for  i in (train['Ratings'].unique()):
    train['Ratings'] = train['Ratings'].replace(i,str(i).split(' ')[0])

pattern2=r'\,'
for  i in (train['Ratings'].unique()):
    if(re.search(pattern2,str(i))):
        train['Ratings'] = train['Ratings'].replace(i,re.sub(pattern2,'',i))

train['Ratings']=train['Ratings'].astype(float)

#######################################################################
genre=[]
len_genre=[]
for i in train['Genre'].unique():
    genre.append(i)

for i in range(0,len(genre)):
    len_genre.append(i)

for i,j in zip(genre,len_genre):
    train['Genre']=train['Genre'].replace(i,j)
############################################################################
category=[]
len_category=[]
for i in train['BookCategory'].unique():
    category.append(i)
for i in range(0,len(category)):
    len_category.append(i)
for i,j in zip(category,len_category):
    train['BookCategory']=train['BookCategory'].replace(i,j)


##########################################################################
author=[]
len_author=[]
for i in train['Author'].unique():
    author.append(i)
for i in range(0,len(author)):
    len_author.append(i)
for i,j in zip(author,len_author):
    train['Author']=train['Author'].replace(i,j)

#######################################

