import dill
import re
stopwords=['wheat','durum','semolina','farina','wheatberry','wheatberries','emmer','spelt','farro','graham','einkorn','rye','pastry','pastries','croissant','pita','naan','bagel','flatbread','cornbread','pretzel','goldfish','cake','cookie','crust','brownie','barley','triticale','malt','yeast','pasta','noodle','ramen','udon','soba','chow','mein','bread','pastry','muffin','donut','doughnut','roll','pancake','waffle','toast','crepe','biscuit','breadcrumb','stuffing','dressing','soy','tortilla','beer']
rcp_data=[]
gf=[]
ngf=[]

with open('recipe_data1.dill','rb') as f:
    rcp_data=dill.load(f)
with open('recipe_data2.dill','rb') as f:
    rcp_data2=dill.load(f)
with open('recipe_data3.dill','rb') as f:
    rcp_data3=dill.load(f)
with open('recipe_data4.dill','rb') as f:
    rcp_data4=dill.load(f)
with open('recipe_data5.dill','rb') as f:
    rcp_data5=dill.load(f)
print("done reading")
for row in rcp_data2:
    rcp_data.append(row)
for row in rcp_data3:
    rcp_data.append(row)
for row in rcp_data4:
    rcp_data.append(row)
for row in rcp_data5:
    rcp_data.append(row)
print("done appending")
print("Total number of recipes is %d" %len(rcp_data))

for ind in range(len(rcp_data)):
    #print(ind)
    row1=rcp_data[ind]
    row_list=row1.split('sep')
    level=row_list[5]
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
        gf.append(rlink)
    elif flag == 1:
        ngf.append(rlink)
    #print(row1)
#for row in gf:
#    print(row)
#    print()

print("Number of Gluten free recipes is %d" %len(gf))
print("Number of recipes containing gluten is %d" %len(ngf))
