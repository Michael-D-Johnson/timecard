from app import app,models,db
from datetime import timedelta,datetime
from flask import render_template

timetable = models.TimeSheet 

def query_all(table,**kwargs):
    all = table.query.all()
    q_list = [i.__dict__ for i in all]
    return q_list

def add_time(**kwargs):
    now = datetime.now()
    date = now.date()
    hourmin = "%s:%s" % (str(now.hour).zfill(2),str(now.minute).zfill(2))
    search = timetable.query.filter_by(date=date).order_by('-id').first()
    if search: 
        if search.date:
            if search.end: 
                new_start = timetable(**{'date':date,'start':hourmin})
                db.session.add(new_start)
            else: 
                search.end = hourmin
                startdatestring = "%s %s" % (search.date,search.start)
                startdate = datetime.strptime(startdatestring,"%Y-%m-%d %H:%M")
                total_time = now - startdate 
                total_hours = total_time.total_seconds()/3600
                search.total = format(total_hours,'.3f')
    else:
        new_start = timetable(**{'date':date,'start':hourmin})
        db.session.add(new_start)
    db.session.commit()
