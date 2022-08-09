# print the bills due this week
# print the bills due the next 4 weeks

from decimal import *
from billDatabase import *
from jobDatabase import *
from paycheckDatabase import *
from datetime import *

today = date.today()
thisMonth = date.today().month
thisYear = date.today().year
thisDay = date.today().day


#----------------------------------------------------------
# 'get' functions

#returns list of bills
def getBillList():
    return billList

def getBillListShort():
    # returns tuples of each bill, [name, cost, dueDate]
    billListShort =  []
    for bill in billList:
        billListShort.append(bill.shortMsg())
    return billListShort

#returns list of paychecks
def getPaycheckList():
    return paycheckList

#returns current job. True for Joe's current job, False for Elizabeth's
def getCurrentJob(isJoes = True):
    if isJoes:
        return JcurrentJob
    else:
        return EcurrentJob



#---------------------------------------------------------
# Prediction functions

def expectedIncome():
    estimatedIncome = 0
    estimatedIncome += joeDefaultCheck.amount * 2
    estimatedIncome += ElizDefaultCheck.amount *2
        
    return estimatedIncome

def expectedCost():
    estimatedCost = 0
    for bill in billList:
        estimatedCost += bill.cost
    
    return estimatedCost

def expectedProfit():
    income = expectedIncome()
    expenses = expectedCost()
    profit = round(income - expenses)

    return profit

#----------------------------------------------------------
# Date range functions

def dateifier(dateify, month = date.today().month, year = date.today().year,):

    try:
        dateified = date(year, month, dateify)
    except: 
        if month == 2:
            dateify = 28
        else :
            dateify = 30
        
        dateified = date(year, month, dateify)


    return dateified

#calculates range from today
#use range in days
def dateRangeCalc(range, begindate = today):
    rangeEnd = begindate + timedelta(days=range)
    return rangeEnd

def billsDueCalc(range, begindate = today):
    rangeEnd = dateRangeCalc(range, begindate)
    billsDue = []

    for bill in billList:
        dueDateThisMonth = dateifier(bill.dueDate, begindate.month, begindate.year)
        dueDateNextMonth = dateifier(bill.dueDate, rangeEnd.month, rangeEnd.year)
        if dueDateThisMonth >= begindate and dueDateThisMonth <= rangeEnd:
            billsDue.append(bill)
        elif dueDateNextMonth >= begindate and dueDateNextMonth <= rangeEnd:
            billsDue.append(bill)
    
    return billsDue
        


def billsDue():
    pass



#----------------------------------------------------------------------------------------------------------------
# Tester section, to make sure these functions work!
# print(getBillList())
# print(getBillListShort())
# print(getPaycheckList())
# print(getCurrentJob(True))
# print(getCurrentJob(False))
# print(expectedIncome())
# print(expectedCost())
# print(expectedProfit())
#print(dateifier(12))
#print(dateRangeCalc(14))
#print(billsDueCalc(14))
#print(dateRangeCalc(16, date(2022, 8, 28)))
print(billsDueCalc(7, dateifier(2022, 2, 31)))