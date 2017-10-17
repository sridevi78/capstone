import dill
import re
stopwords=['worcestershire','chicken','fish','tilapia','shrimp','scallop','salmon','scallop','salmon','haddock','beef','lamb','goat','bison','turkey','pork','bacon','ham','dog','prosciutto','salami','sausage','mutton','venison','duck','boar','anchovies','swordfish','tuna','trout','cod','sardine','bass','catfish','flounder','grouper','hallibut','herring','mahi','snapper','lobster','squid','oyster']
rcp_data=[]
veg=[]
nonveg=[]

with open('recipe_data1.dill','rb') as f:
    rcp_data=dill.load(f)
with open('recipe_data2.dill','rb') as f:
    rcp_data2=dill.load(f)
with open('recipe_data3.dill','rb') as f:
    rcp_data3=dill.load(f)
with open('recipe_data4.dill','rb') as f:
    rcp_data4=dill.load(f)
print("done reading")
for row in rcp_data2:
    rcp_data.append(row)
for row in rcp_data3:
    rcp_data.append(row)
for row in rcp_data4:
    rcp_data.append(row)
print("done appending")
print("Total number of recipes is %d" %len(rcp_data))

for ind in range(len(rcp_data)):
    print(ind)
    row1=rcp_data[ind]
    row_list=row1.split('sep')
    ing=row_list[6]
    ing1=ing.split(',')
    rlink=row_list[8]
    flag = 0
    for jj in range(len(ing1)):
        ing2=ing1[jj].split(" ")
        for ii in range(len(ing2)):
            if ing2[ii].strip():
                word1=re.sub("[^a-z0-9.A-Z]+", "", ing2[ii].strip())
                for sword in stopwords:
                    if word1.lower() == str(sword).lower():
                        flag=1
    if flag == 0:
        veg.append(rlink)
    elif flag == 1:
        nonveg.append(rlink)
print("Number of veg recipes is %d" %len(veg))
print("Number of non-veg recipes is %d" %len(nonveg))
