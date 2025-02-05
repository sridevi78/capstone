from flask import Flask, render_template, request, redirect
import flask

app = Flask(__name__)

#This app uses recipe data from the Food Network website to list recipes for people with diet restrictions
@app.route('/')

def index():
    import numpy as np
    import pandas as pd
    import requests
    from datetime import datetime
    from bokeh.io import curdoc
    from bokeh.layouts import row, widgetbox
    from bokeh.models import ColumnDataSource, DatetimeTickFormatter
    from bokeh.models.widgets import Slider, TextInput
    from bokeh.plotting import figure
    from bokeh.embed import components
    from bokeh.resources import INLINE
    from bokeh.util.string import encode_utf8
    import re
    import dill
    import unicodedata
    urls1=[]
    lvl={}    

    #reading user allergy information and recipe preferences
    args = flask.request.args
    milk = request.args.get('milk')
    eggs = request.args.get('eggs')
    pnut = request.args.get('peanuts')
    tnuts = request.args.get('treenuts')
    wheat = request.args.get('wheat')
    soy = request.args.get('soy')
    fish = request.args.get('fish')
    sfish = request.args.get('sfish')
    sesame = request.args.get('sesame')
    item1 = request.args.get('Item_1')
    item2 = request.args.get('Item_2')
    item3 = request.args.get('Item_3')
    item4 = request.args.get('Item_4')

#stop words for different allergies
    stop1=['butter', 'buttermilk', 'cheese', 'cottage cheese', 'cream','curds','custard','ghee','ice cream','half and half','pudding','sour cream','whey','yoghurt']
    stop2=['eggs','egg','eggnog','mayo','mayonnaise','meringue','marshmallow','egg substitute','ice cream','nougat']
    stop3=['peanut','peanut oil','beer nuts','ground nuts','peanut butter','peanut flour']
    stop4=['almond','beechnut','brazil nut','butternut','cashew','chestnut','coconut','hazelnut','macadamia','marzipan','almond paste','cashew butter','almond butter','peanut butter','almond milk','cashew milk','walnut oil','almond oil','pecan','pesto','pine nut','pistachio','praline','walnut']
    stop5=['edamame','soy','soya','soy bean','soy protein','soy sauce','tofu']
    stop6=['bread crumbs','bulgur','couscous','durum','farina','flour','all-purpose','bread','cake','graham','pastry','self-rising','wheat','whole wheat','pasta','seitan','semolina','soy sauce']
    stop7=['anchovies','bass','catfish','cod','flounder','grouper','haddock','hake','halibu','herring','mahi mahi','perch','pike','pollock','salmon','scrod','sole','snapper','swordfish','tilapia','trout','tuna','fish oil','fish sticks','fish','barbecue sauce','caesar dressing','caesar salad','worcestershire sauce']
    stop8=['barnacle','crab','crawfish','krill','lobster','prawns','shrimp','clams','mussels','scallops','snails','squid']
    stop9=['gingelly oil','sesame flour','sesame oil','sesame paste','sesame salt','sesame seed','tahini','til']
    aller=""
    stopwords=[]
    
    #picking the right stop words depending on the user's allergies
    if milk:
        aller="milk"
        for wd in stop1:
            stopwords.append(wd)
    if eggs:
        aller="eggs"
        for wd in stop2:
            stopwords.append(wd)
    if pnut:
        aller="peanuts"
        for wd in stop3:
            stopwords.append(wd)
    if tnuts:
        aller="treenuts"
        for wd in stop4:
            stopwords.append(wd)
    if wheat:
        aller="wheat"
        for wd in stop5:
            stopwords.append(wd)
    if soy:
        aller="soy"
        for wd in stop6:
            stopwords.append(wd)
    if fish:
        aller="fish"
        for wd in stop7:
            stopwords.append(wd)
    if sfish:
        aller="shellfish"
        for wd in stop8:
            stopwords.append(wd)
    if sesame:
        aller="sesame"
        for wd in stop9:
            stopwords.append(wd)

    #storing user preferences
    co_ti="Under 15 minutes"   
    ll="easy"
    rr="4+ stars"
    cct="Main Dish"
    if stopwords:
        if 'le15' in item1:
            co_ti="Under 15 minutes"
        if 'le30' in item1:
            co_ti="Under 30 minutes"
        if 'le45' in item1:
            co_ti="Under 45 minutes"
        if 'le60' in item1:
            co_ti="Under 60 minutes"
        if 'gt60' in item1:
            co_ti="Over 60 minutes"
        if 'ea' in item3:
            ll="easy"
        if 'in' in item3:
            ll="intermediate"
        if 'di' in item3:
            ll="advanced"
        if 'ge4' in item2:
            rr="4+ stars"
        if 'ge3' in item2:
            rr="3+ stars"
        if 'ge2' in item2:
            rr="2+ stars"
        if 'ge1' in item2:
            rr="1+ stars"
        if 'ge0' in item2:
            rr="0+ stars"
        if 'md' in item4:
            cct="Main Dish"
        if 'app' in item4:
            cct="Appetizer"
        if 'dess' in item4:
            cct="Dessert"
        #print "found stopwords"

        #reading recipe data from files 
        rcp_data=[]
        with open('recipe_datav21.dill','r') as f:
            rcp_data=dill.load(f)
        with open('recipe_datav22.dill','r') as f:
            rcp_data2=dill.load(f)
        with open('recipe_datav23.dill','r') as f:
            rcp_data3=dill.load(f)
        with open('recipe_datav24.dill','r') as f:
            rcp_data4=dill.load(f)
        with open('recipe_datav25.dill','r') as f:
            rcp_data5=dill.load(f)
        with open('recipe_datav26.dill','r') as f:
            rcp_data6=dill.load(f)
        with open('recipe_datav27.dill','r') as f:
            rcp_data7=dill.load(f)

        #storing the recipe info from the different files into a single list rcp_data
        for row in rcp_data2:
            rcp_data.append(row)
        for row in rcp_data3:
           rcp_data.append(row)
        for row in rcp_data4:
           rcp_data.append(row)
        for row in rcp_data5:
           rcp_data.append(row)
        for row in rcp_data6:
           rcp_data.append(row)
        for row in rcp_data7:
           rcp_data.append(row)
        print len(rcp_data)

        
        for ind in range(len(rcp_data)): 
           #extracting each recipe's information
           row1=rcp_data[ind]
           #print "***********************************************"
           #print row1.encode('utf-8')
           row_list=row1.split('sep')
           title=re.sub("[^a-z0-9. A-Z]+", "",row_list[0])
           title=title.replace('"', "").strip()
           chef=re.sub("[^a-z0-9. A-Z]+", "", row_list[1])
           chef=chef.replace('"', "").strip()
           rating=row_list[2].replace('"', "").strip()
           review=row_list[3].replace('"', "").strip()
           cook_time=re.sub("[^a-z0-9. A-Z]+", "", row_list[4])
           cook_time=row_list[4].replace('"', "").strip()
           level=re.sub("[^a-z0-9. A-Z]+", "", row_list[5])
           level=level.replace('"', "").strip()
           if level.lower() in lvl.keys():
               lvl[level.lower()]+=1
           else:
               lvl[level.lower()]=1            
           print level.lower()
           ing=row_list[6]
           #print "title is %s" %title
           #print "chef is %s" %chef
           #print "rating is %s" %rating
           if review == "":
               review="0"

           #print "reviews are %s" %review
           #print "***********************************************"
           ctime=str(cook_time).split('H')
           #print ctime
           try:
               ctime0=re.sub("[^0-9]+", "", ctime[0])
               ctime1=re.sub("[^0-9]+", "", ctime[1])
           except:
               continue
           ct=60*int(ctime0)+int(ctime1)
           #print "cook time is %d" %ct
           #print "level is %s" %level
           cat=row_list[7].split(',')
           #print "category is %s" %cat.encode('utf-8')
           rlink=row_list[8]
           #print "recipe link is %s" %rlink
                     


           #checking if the recipe meets user selected preferences
           flag=0
       
           if 'le15' in item1:
               if ct > 15:
                   flag=1
           if 'le30' in item1:
               if ct > 30:
                   flag=1
           if 'le45' in item1:
               if ct > 45:
                   flag=1
           if 'le60' in item1:
               if ct >60:
                   flag=1
           if 'ea' in item3:
               if 'easy' not in level.lower():
                   flag=1
           if 'in' in item3:
               if 'intermediate' not in level.lower():
                   flag=1
           if 'ad' in item3:
               if 'advanced' not in level.lower():
                   flag=1
           if 'ge4' in item2:
               if rating < 4.0:
                   flag=1
           if 'ge3' in item2:
               if rating < 3.0:
                   flag=1
           if 'ge2' in item2:
               if rating < 2.0:
                   flag=1
           if 'ge1' in item2:
               if rating < 1.0:
                   flag=1
           if 'ge0' in item2:
               if rating <=0.0:
                   flag=1
           fl=0
           #print level            
           if 'md' in item4:
               for cc in range(len(cat)):
                   #print cat[cc].encode('utf-8').lower()
                   if 'main dish' in cat[cc].encode('utf-8').lower():
                       #print "found"
                       fl=1 
               if fl == 0:
                   flag=1
           if 'app' in item4: 
               for cc in range(len(cat)):
                   #print cat[cc].encode('utf-8').lower()
                   if 'appetizer' in cat[cc].encode('utf-8').lower():
                      #print "found"
                      fl=1    
               if fl == 0:
                   flag=1 
           if 'dess' in item4: 
               for cc in range(len(cat)):
                   #print cat[cc].encode('utf-8').lower()
                   if 'dessert' in cat[cc].encode('utf-8').lower():
                      #print "found"
                      fl=1    
               if fl == 0:
                   flag=1
           if flag == 1:
               continue
           else:
               #Ensuring the recipe is suitable for the user depending on the selected allergen
               ing1=ing.split(',')
               for jj in range(len(ing1)):
                   #print ing1[jj]
                   ing2=ing1[jj].split(" ")
                   #print "from here"
                   for ii in range(len(ing2)):
                       if ing2[ii].strip():
                           word1=re.sub("[^a-z0-9.A-Z]+", "", ing2[ii].strip())
                           for sword in stopwords:
                               #print word1.lower(),str(sword).lower()
                               if word1.lower() == str(sword).lower():
                                   flag=1
           #If recipe is not a fit, continue
           if flag == 1:
               continue
           else:
           #If the recipe is a fit, append it to a list
               #print rlink
               urls1.append((rlink,title,int(review)))
    #print "out of the loop"
    #print urls1
    output=[]
    if len(urls1) == 0:
        print "here"
        output.append(("","no results found",""))
    else:
        #Display the top 10 recipes based on the number of reviews
        output = sorted(urls1, key=lambda x: x[-1],reverse=True)[:10]
    
    pref="Allergic to: %s," %aller+" Cooktime: %s," %co_ti+" Recipe Level: %s," %ll+" Rating: %s," %rr+" Recipe Category: %s" %cct
    print output    
    print lvl
    print "reached end"
    js_resources = INLINE.render_js()
    css_resources = INLINE.render_css()
    html = flask.render_template(
           'index.html',
           js_resources=js_resources,
           css_resources=css_resources,
           _milk=milk,
           _eggs=eggs,
           _pnut=pnut,
           _tnuts=tnuts,
           _wheat=wheat,
           _soy=soy,
           _fish=fish,
           _sfish=sfish,
           _sesame=sesame,
           _urls=output,
           _pref=pref
     )
    return encode_utf8(html)


if __name__ == '__main__':
  app.run(port=33507)
