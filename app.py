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

  args = flask.request.args

  # Get all the form arguments in the url with defaults
  tick = str(getitem(args, '_ticker', 0))
 
  #requests and JSON
  import quandl
  quandl.ApiConfig.api_key = 'LBx4fXSMArrNorDxMc49'
  data=quandl.get_table('WIKI/PRICES',ticker=tick)
  data_new=data[(datetime.now().date()-data['date']).apply(lambda x: float(x.days)) <=31.0]
  #print data_new

  sm_date=list(data_new['date'])
  sm_open=list(data_new['open'])
  sm_close=list(data_new['close'])
  sm_adjopen=list(data_new['adj_open'])
  sm_adjclose=list(data_new['adj_close'])


  p = figure(
     tools="pan,box_zoom,reset,save",
     y_axis_type="linear",title="Stock Market Prices for  %s" %tick,
     x_axis_label='Date', y_axis_label='Price'
  )

  # add a line renderer with legend and line thickness
  p.line(sm_date, sm_open, line_color="red", legend="Opening", line_width=2)
  p.line(sm_date, sm_close, line_color="green", legend="Closing",line_width=2)
  p.line(sm_date, sm_adjopen, line_color="blue", legend="Adjusted Opening",line_width=2)
  p.circle(sm_date, sm_adjopen, line_color="blue", fill_color="blue",legend="Adjusted Opening", line_width=2)
  p.line(sm_date, sm_adjclose, line_color="orange", legend="Adjusted Closing",line_width=2)
  p.circle(sm_date, sm_adjclose, line_color="orange", fill_color="orange",legend="Adjusted Closing", line_width=2)

  p.xaxis.formatter=DatetimeTickFormatter(
          hours=["%d %B %Y"],
          days=["%d %B %Y"],
          months=["%d %B %Y"],
          years=["%d %B %Y"],
      )  
  js_resources = INLINE.render_js()
  css_resources = INLINE.render_css()  
  script, div = components(p)
  html=render_template("index.html", script=script, div=div,js_resources=js_resources,
        css_resources=css_resources)
  return encode_utf8(html)

if __name__ == '__main__':
  app.run(port=33507)
