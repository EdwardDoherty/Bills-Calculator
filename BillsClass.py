
# Creates the Bill() class, which keeps track of:
# Bill name
# Bill cost
# Due Date
# Bill Type (credit card, insurance, utility, etc)
# Grace Period in # of days allowed
# Interest rate, when applicable
# Notes

class Bill:

    def __init__(self, name = "not entered", cost = 0, dueDate = 1, billType = "not entered", gracePeriod = 0, interestRate  = 0, notes = "No notes"):
        self.name = name
        self.cost = cost
        self.dueDate = dueDate
        self.billType = billType
        self.gracePeriod = gracePeriod
        self.interestRate = interestRate
        self.notes = notes
    
    def __repr__(self) -> str:
        msg = """
        {name} | ${cost}, Due {dueDate}, Type: {billType}, Grace Period: {gracePeriod}, Interest Rate: {interestRate}, Notes: '{notes}'
        """.format(name=self.name, cost=self.cost, dueDate=self.dueDate, billType=self.billType, gracePeriod=self.gracePeriod, interestRate=self.interestRate, notes=self.notes)
        return msg

