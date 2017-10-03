from flask import Flask, render_template, request, redirect
import flask

app = Flask(__name__)


@app.route('/')

def index():
    url=[]
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

    print item1
    print item2
    print item3
    stop1=['butter', 'buttermilk', 'cheese', 'cottage cheese', 'cream','curds','custard','ghee','ice cream','half and half','pudding','sour cream','whey','yoghurt']
    stop2=['egg','eggnog','mayo','mayonnaise','meringue','marshmallow','egg substitute','ice cream','nougat']
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
        print stopwords
        rcp_data = pd.read_csv('recipe_data1.csv',"error_bad_lines = False")
        #print len(rcp_data.itertuples(name='Pandas'))
        print rcp_data.iloc[:10]
        for ind in range(len(rcp_data)): 
            #rcp_data.itertuples(name='Pandas'):
            #print "inside the for loop"
            #print index,row
            row=rcp_data.iloc[ind]
            print row
            row_list=str(row).split('[')
            info1=row_list[1].split(',')
            #print info1
            #print "that was info1"
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
            #print info2
            #print "that was info2"
            #print title,chef,rating,cook_time,level
            ing=info2[0]
            try:
                rlink=info2[1].replace(",","").strip()
            except:
                continue
            #print rlink
            flag=0
            for word in ing:
                if word in stopwords:
                    flag=1
                else:
                    urls.append(rlink)
            if flag == 1:
                continue
            if len(urls) >= 10:
                break
        #print urls       
    print "reached end"
    p = figure(
        tools="pan,box_zoom,reset,save",
        y_axis_type="linear",title="Stock Market Prices for  GOOG",
        x_axis_label='Date', y_axis_label='Price'
    )

    js_resources = INLINE.render_js()
    css_resources = INLINE.render_css()
    script, div = components(p)
    html = flask.render_template(
           'index.html',
           plot_script=script,
           plot_div=div,
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
           _sesame=sesame
          )
    return encode_utf8(html)



if __name__ == '__main__':
  app.run(port=33507)
