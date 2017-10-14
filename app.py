from flask import Flask, render_template, request, redirect
import flask

app = Flask(__name__)


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
    import csv
    import unicodedata
    urls1=[]
    
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

    stop1=['butter', 'buttermilk', 'cheese', 'cottage cheese', 'cream','curds','custard','ghee','ice cream','half and half','pudding','sour cream','whey','yoghurt']
    stop2=['eggs','egg','eggnog','mayo','mayonnaise','meringue','marshmallow','egg substitute','ice cream','nougat']
    stop3=['peanut','peanut oil','beer nuts','ground nuts','peanut butter','peanut flour']
    stop4=['almond','beechnut','brazil nut','butternut','cashew','chestnut','coconut','hazelnut','macadamia','marzipan','almond paste','cashew butter','almond butter','peanut butter','almond milk','cashew milk','walnut oil','almond oil','pecan','pesto','pine nut','pistachio','praline','walnut']
    stop5=['edamame','soy','soya','soy bean','soy protein','soy sauce','tofu']
    stop6=['bread crumbs','bulgur','couscous','durum','farina','flour','all-purpose','bread','cake','graham','pastry','self-rising','wheat','whole wheat','pasta','seitan','semolina','soy sauce']
    stop7=['anchovies','bass','catfish','cod','flounder','grouper','haddock','hake','halibu','herring','mahi mahi','perch','pike','pollock','salmon','scrod','sole','snapper','swordfish','tilapia','trout','tuna','fish oil','fish sticks','fish','barbecue sauce','caesar dressing','caesar salad','worcestershire sauce']
    stop8=['barnacle','crab','crawfish','krill','lobster','prawns','shrimp','clams','mussels','scallops','snails','squid']
    stop9=['gingelly oil','sesame flour','sesame oil','sesame paste','sesame salt','sesame seed','tahini','til']

    stopwords=[]
    if milk:
        stopwords.append(stop1)
    if eggs:
        stopwords.append(stop2)
    if pnut:
        stopwords.append(stop3)
    if tnuts:
        stopwords.append(stop4)
    if wheat:
        stopwords.append(stop5)
    if soy:
        stopwords.append(stop6)
    if fish:
        stopwords.append(stop7)
    if sfish:
        stopwords.append(stop8)
    if sesame:
        stopwords.append(stop9)
    if stopwords:
        print "found stopwords"
        f = open('recipe_data21.csv')
        csv_f = csv.reader(f)
        rcp_data=[]
        for row in csv_f:
            rcp_data.append(row)
     
        for ind in range(len(rcp_data)): 
            row1=rcp_data[ind]
            #print row1
            row_list=str(row1).split('[')
            #print row_list
            #print "split by ["
            info1=row_list[2].split(',')
            #print info1
            #print "second element split by ,"
            info1[0]=re.sub("[^a-z0-9. A-Z]+", "", info1[0])
            title=info1[0].replace('"', "").strip()
            #print type(title)
            info1[1]=re.sub("[^a-z0-9. A-Z]+", "", info1[1])
            chef=info1[1].replace('"', "").strip()
            info1[2]=re.sub("[^a-z0-9. A-Z]+", "", info1[2])
            try:
                rating=float(info1[2].replace('"', "").strip())
            except:
                continue
            #print "checkpoint 1"
            info1[3]=re.sub("[^a-z0-9. A-Z]+", "", info1[3])
            review=info1[3].replace('"', "").strip()
            info1[4]=re.sub("[^a-z0-9. A-Z]+", "", info1[4])
            cook_time=info1[4].replace('"', "").strip()
            info1[5]=re.sub("[^a-z0-9. A-Z]+", "", info1[5])
            level=info1[5].replace('"', "").strip()
            info2=row_list[3].split(']')
            link=row_list[4][2]
            ing=info2[0]
            print row_list[-1]
            try:
                rlink2=info2[1].replace(",","").strip().split("'")
                rlink=rlink2[1]
            except:
                continue
            
            print "checkpoint2"          
            flag=0
            ctime=str(cook_time).split('H')
            ctime0=re.sub("[^0-9]+", "", ctime[0])
            ctime1=re.sub("[^0-9]+", "", ctime[1])
            level1=str(level)[1:]
            ct=60*int(ctime0)+int(ctime1)
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
            if 'ea' in item2:
                if 'easy' not in level1.lower():
                    flag=1
            if 'me' in item2:
                if 'medium' not in level1.lower():
                    flag=1
            if 'di' in item2:
                if 'difficult' not in level1.lower():
                    flag=1
            if 'ge4' in item3:
                if rating < 4.0:
                    flag=1
            if 'ge3' in item3:
                if rating < 3.0:
                    flag=1
            if 'ge2' in item3:
                if rating < 2.0:
                    flag=1
            if 'ge1' in item3:
                if rating < 1.0:
                    flag=1
            if 'ge0' in item3:
                if rating <=0.0:
                    flag=1
             
            #print ing
            #print "those were ingredients"
            for words in ing.split(','):
                for word in words.split(' '):
                    word=re.sub("[^a-z0-9. A-Z]+", "", word)
                    #print word
                    #print "that was one word"
                    for sword in stopwords:
                        if word.lower() in str(sword).lower() and flag==0:
                            flag=1
            print flag
            print "that was flag"
            
            if flag == 1:
                continue
            else:
                print item1
                print item2
                print item3
                print "Those were the preferences"
                #print "**************************"
                #print ct
                #print rating
                #print level1.lower()
                #print title
                print rlink
                urls1.append((rlink,title,review))
                
    output = sorted(urls1, key=lambda x: x[-1])[:10]
    print output
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
           _urls=output
          )
    return encode_utf8(html)



if __name__ == '__main__':
  app.run(port=33507)
