from flask import Flask, render_template, request, redirect
import flask

app = Flask(__name__)


@app.route('/', methods=['POST','GET'])
def index():
  if request.method == 'POST':
      import numpy as np
      import pandas as pd
      import requests
      import re
      from datetime import datetime
      from bokeh.layouts import row, widgetbox
      from bokeh.models import ColumnDataSource, DatetimeTickFormatter
      from bokeh.models.widgets import Slider, TextInput
      import csv
      milk = request.form['milk']
      print milk
      print "that was milk"
      eggs = request.form['eggs']
      print eggs
      print "that was eggs"
      pnut = request.form['peanuts']
      tnuts = request.form['treenuts']
      wheat = request.form['wheat']
      soy = request.form['soy']
      fish = request.form['fish']
      sfish = request.form['sfish']
      sesame = request.form['sesame']
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
          print stopwords
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
      rcp_data = pd.read_csv('recipe_data1.csv',"error_bad_lines = False")
       
      urls=[]
      for index,row in rcp_data.itertuples(index=True, name='Pandas'):
          print "inside the for loop"
          row_list=str(row).split('[')
          info1=row_list[1].split(',')
          print info1
          print "that was info1"
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
          print info2
          print "that was info2"
          ing=info2[0]
          try:
              rlink=info2[1].replace(",","").strip()
          except:
              continue
          flag=0
          for word in ing:
              if word in stopwords:
                  flag=1
                  break
              else:
                  urls.append(rlink)
          if flag == 1:
              continue 
          elif len(urls) >= 10:
              break
      return 'OK'             
  elif request.method == 'GET':
      return render_template('index.html')
  
if __name__ == '__main__':
  app.run(port=33507) 
