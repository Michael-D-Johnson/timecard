#!/usr/bin/env python

from datetime import timedelta
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__,template_folder="../templates")
app.config.from_envvar('TIMECARD_CONFIG')
app.secret_key = app.config['SECRET_KEY']

db = SQLAlchemy(app)

from app import models,views
