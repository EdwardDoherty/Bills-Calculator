# print the bills due this week
# print the bills due the next 4 weeks

from decimal import *
from billDatabase import *
from jobDatabase import *
from paycheckDatabase import *



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






#----------------------------------------------------------------------------------------------------------------
# Tester section, to make sure these functions work!
print(getBillList())
print(getBillListShort())
print(getPaycheckList())
print(getCurrentJob(True))
print(getCurrentJob(False))
print(expectedIncome())
print(expectedCost())
print(expectedProfit())