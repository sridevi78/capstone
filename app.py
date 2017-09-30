from flask import Flask, render_template, request, redirect
import flask

app = Flask(__name__)

@app.route('/')


def index():
  import numpy as np
  import pandas as pd
  import requests
  from datetime import datetime
  from bokeh.layouts import row, widgetbox
  from bokeh.models import ColumnDataSource, DatetimeTickFormatter
  from bokeh.models.widgets import Slider, TextInput
  from bokeh.plotting import figure
  from bokeh.embed import components
  from bokeh.resources import INLINE
  from bokeh.util.string import encode_utf8
  import csv
  args = flask.request.args
  milk = args.get('milk') 
  eggs = args.get('eggs')
  pnut = args.get('peanuts')
  tnuts = args.get('treenuts')
  wheat = args.get('wheat')
  soy = args.get('soy')
  fish = args.get('fish')
  sfish = args.get('sfish')
  sesame = args.get('sesame')

  rcp_data = pd.read_csv('recipe_data1.csv',"error_bad_lines = False")
  for i in range(len(rcp_data)):
      print str(rcp_data.iloc[i])
      print "***************" 
  print len(rcp_data)
  
  p = figure(
     tools="pan,box_zoom,reset,save",
     y_axis_type="linear",title="",
     x_axis_label='Date', y_axis_label='Price'
  )

  # add a line renderer with legend and line thickness
  #if milk:
  #if eggs:
  #if pnut:
  #if tnuts:
  #if wheat:
  #if soy:
  #if fish:
  #if sfish:
  #if sesame:

  p.xaxis.formatter=DatetimeTickFormatter(
          hours=["%d %B %Y"],
          days=["%d %B %Y"],
          months=["%d %B %Y"],
          years=["%d %B %Y"],
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
