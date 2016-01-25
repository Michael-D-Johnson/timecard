import os
from datetime import timedelta

basedir = os.getenv('TIMECARD_DIR')

DB_DIR = os.path.join(basedir,'db')

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(DB_DIR, 'timecard.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(DB_DIR, 'repository')

WTF_CSRF_ENABLED = True
SECRET_KEY = 'GrGr!$!$BAba'
