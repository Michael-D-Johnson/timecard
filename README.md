#Setup:
1. Clone repository:
git clone https://github.com/Michael-D-Johnson/timecard.git


2. Add following variables to environment
        TIMECARD_DIR # directory to repository
        TIMECARD_CONFIG # full path to config file

3. Setup db:
       python bin/create_db.py

4. "Clock-in" and "Clock-out":
       ./report

5. Run flask:
       python run_server.py
