import pandas as pd
import numpy as np
import csv
import re
f = open('recipe_data1.csv')
csv_f = csv.reader(f)
rcp_data=[]
for row in csv_f:
  rcp_data.append(row)
for ind in range(len(rcp_data)):
    row1=rcp_data[ind]
    print(row1)
    row_list=str(row1).split('[')
    print(row_list)
    print("split by [")
    info1=row_list[1].split(',')
    print(info1)
    print("second element split by ,")
    info1[0]=re.sub("[^a-z0-9. A-Z]+", "", info1[0])
    title=info1[0].replace('"', "").strip()
    info1[1]=re.sub("[^a-z0-9. A-Z]+", "", info1[1])
    chef=info1[1].replace('"', "").strip()
    info1[2]=re.sub("[^a-z0-9. A-Z]+", "", info1[2])
    rating=info1[2].replace('"', "").strip()
    info1[3]=re.sub("[^a-z0-9. A-Z]+", "", info1[3])
    review=info1[3].replace('"', "").strip()
    info1[4]=re.sub("[^a-z0-9. A-Z]+", "", info1[4])
    cook_time=info1[4].replace('"', "").strip()
    info1[5]=re.sub("[^a-z0-9. A-Z]+", "", info1[5])
    level=info1[5].replace('"', "").strip()
    info2=row_list[2].split(']')
    print(info2)
    ing=info2[0]
    try:
        rlink=info2[1].replace(",","").strip()
    except:
        continue
    flag=0
    for word in ing:
        if word in stopwords and flag==0:
            flag=1
    if flag == 1:
        continue
    else:
        urls.append(rlink)
