from flask import Flask, render_template, request, redirect
import flask

app = Flask(__name__)
def getitem(obj, item, default):
    if item not in obj:
        return default
    else:
        return obj[item]

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
  tick = str(getitem(args, '_tick', 'GOOG'))
  #open1 = flask.request.form.get('_open') 
  #selected = flask.request.form.getlist('check')
  #any_selected = bool(selected)
  #close = flask.request.form.get('_close') 
  #aopen = flask.request.form.get('_aopen') 
  #aclose = flask.request.form.get('_aclose') 
  #formData = flask.request.values  
  open1 = flask.request.form.get('_mpen')
  close = flask.request.form.get('_close')
  aopen = flask.request.form.get('_aopen')
  aclose = flask.request.form.get('_aclose')
  value1= u"_open" in args 
  print tick, value1

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
  if open1 == 'checked':
      p.line(sm_date, sm_open, line_color="red", legend="Opening", line_width=2)
  if close == 'checked':
      p.line(sm_date, sm_close, line_color="green", legend="Closing",line_width=2)
  if aopen == 'checked':
      p.line(sm_date, sm_adjopen, line_color="blue", legend="Adjusted Opening",line_width=2)
      p.circle(sm_date, sm_adjopen, line_color="blue", fill_color="blue",legend="Adjusted Opening", line_width=2)
  if aclose == 'checked':
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
  html = flask.render_template(
        'index.html',
        plot_script=script,
        plot_div=div,
        js_resources=js_resources,
        css_resources=css_resources,
        _tick=tick,
        _open=open1,
        _close=close,
        _aopen=aopen,
        _aclose=aclose
       )
  return encode_utf8(html)

if __name__ == '__main__':
  app.run(port=33507)
