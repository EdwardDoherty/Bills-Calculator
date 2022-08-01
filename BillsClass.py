
# Creates the Bill() class, which keeps track of:
# Bill name
# Bill cost
# Due Date
# Bill Type (credit card, insurance, utility, etc)
# Grace Period in # of days allowed
# Interest rate, when applicable
# Notes
from operator import *

billList = []


class Bill:

    def __init__(self, name = "not entered", cost = 0, dueDate = 1, billType = "not entered", gracePeriod = 0, interestRate  = 0, notes = "No notes"):
        self.name = name
        self.cost = cost
        self.dueDate = dueDate
        self.billType = billType
        self.gracePeriod = gracePeriod
        self.interestRate = interestRate
        self.notes = notes

        self.billListAppend()

    def __repr__(self) -> str:
        msg = """
        {name} | ${cost}, Due {dueDate}, Type: {billType}, Grace Period: {gracePeriod}, Interest Rate: {interestRate}, Notes: '{notes}'
        """.format(name=self.name, cost=self.cost, dueDate=self.dueDate, billType=self.billType, gracePeriod=self.gracePeriod, interestRate=self.interestRate, notes=self.notes)
        return msg

    def shortMsg(self) -> str:
        shortMsg = []
        shortMsg.append(self.name)
        shortMsg.append(self.cost)
        shortMsg.append(self.dueDate)
        return shortMsg


    def getCost(self):
        return self.cost



    # 'key' does nothing but is required to make this function work with itemgetter().
    # I need to do some research on this function but for now this works fine even though it's ugly
    def __getitem__(self, key):
        return self.dueDate

    def getDueDate(self):
        return self.dueDate

    def billListAppend(self):
        billList.append(self)
        billList.sort(key=itemgetter(self.dueDate))