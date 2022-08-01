# print the bills due this week
# print the bills due the next 4 weeks

from telnetlib import EC
from billDatabase import *
from jobDatabase import *
from paycheckDatabase import *


#returns list of bills
def getBillList():
    return billList

#returns list of paychecks
def getPaycheckList():
    return paycheckList

#returns current job. True for Joe's current job, False for Elizabeth's
def getCurrentJob(isJoes = True):
    if isJoes:
        return JcurrentJob
    else:
        return EcurrentJob





#----------------------------------------------------------------------------------------------------------------
# Tester section, to make sure these functions work!
print(getBillList())
print(getPaycheckList())
print(getCurrentJob(True))
print(getCurrentJob(False))