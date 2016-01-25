from flask import render_template,request,redirect,session,url_for,flash
from app import app
from app.models import TimeSheet
import pandas
import math

@app.route('/')
@app.route('/index')
def index():   
    return render_template('base.html')

@app.route('/summary')
def summary():
    raw_data = TimeSheet.query.with_entities(TimeSheet.id,
                                         TimeSheet.date,TimeSheet.start,
                                         TimeSheet.end,TimeSheet.total).all()
    df = pandas.DataFrame(raw_data,columns=['id','date','start','end','total'])
    df_grouped = df.groupby('date')
    new_dict = []
    for name,group in df_grouped:
        group_list = list(group['total'].fillna('None').values)
        if 'None' in group_list:
            minutes,hours = 'None','None'
            summation = "NA"
        else:
            summ = group['total'].sum()
            mins,hours = math.modf(summ)
            minutes = format(int(mins*60),'2d')
            hours = format(int(hours),'2d')
            summation = "%s hours %s minutes" % (hours,minutes)
        new_dict.append({'date':name,'total':summation})
    new_df = pandas.DataFrame(new_dict)
    new_df = new_df.sort(columns=['date'])
    columns = new_df.columns

    return render_template('summary.html',columns=columns,df = new_df)

@app.route('/raw')
def raw():
    raw_data = TimeSheet.query.with_entities(TimeSheet.id,
                                         TimeSheet.date,TimeSheet.start,
                                         TimeSheet.end,TimeSheet.total).all()
    df = pandas.DataFrame(raw_data,columns=['id','date','start','end','total'])
    df = df.sort(columns=['id'])
    df = df.fillna('None')
    columns = df.columns

    return render_template('summary.html',columns=columns,df = df)

