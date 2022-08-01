# initialize paycheck objects here
# this is the current database, eventually maybe I'll replace this with a GUI but for now this works fine as I am the only intended user

from PaycheckClass import *
from datetime import *
from jobDatabase import *



joeDefaultCheck = PayCheck(550, date(2022, 7, 14), JcurrentJob.avgHours, JcurrentJob, "JOE DEFAULT PAYCHECK")
ElizDefaultCheck = PayCheck(1130, date(2022, 7, 21), EcurrentJob.avgHours,EcurrentJob, "ELIZABETH DEFAULT CHECK")


# RECORD BILLS HERE
# ALWAYS REMEMBER TO RECORD DATE AS SHOWN BELOW, YEAR, MONTH, DATE
# PayCheck(amount, date, hours, job, notes)
joeCheck1 = PayCheck(614.87, date(2022,7,28), 44.50, homeDepot, "First check entered into this program")


