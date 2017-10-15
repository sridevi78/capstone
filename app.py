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
    import dill
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
        rcp_data=[]
        with open('recipe_data1.dill','r') as f:
             rcp_data=dill.load(f)
        print len(rcp_data)
        for ind in range(len(rcp_data)): 
            row1=rcp_data[ind]
            print row1
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
            ing=row_list[6]
            print "title is %s" %title
            print "chef is %s" %chef
            print "rating is %s" %rating
            print "reviews are %s" %review
            ctime=str(cook_time).split('H')
            ctime0=re.sub("[^0-9]+", "", ctime[0])
            ctime1=re.sub("[^0-9]+", "", ctime[1])
            ct=60*int(ctime0)+int(ctime1)
            print "cook time is %d" %ct
            rlink=row_list[7]
            print "recipe link is %s" %rlink
                      
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
            if 'ea' in item2:
                if 'easy' not in level.lower():
                    flag=1
            if 'me' in item2:
                if 'medium' not in level.lower():
                    flag=1
            if 'di' in item2:
                if 'difficult' not in level.lower():
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
             
            print ing
            print "those were ingredients"
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
