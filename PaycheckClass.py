
# creates the Paycheck() class, which keeps track of
# Whos check it was
# Net revenue. Take home pay
# Date money was received
# Hours you worked this paycheck
# Your hourly wage at this time
# Gross pay, before taxes and deductions

class PayCheck:

    def __init__(self, isJoes, amount, date, hours, wage, gross):
        self.isJoes = isJoes
        self.amount = amount
        self.date = date
        self.hours = hours
        self.wage = wage
        self.gross = gross
        
        if(isJoes):
            self.who = "Joe"
        else: 
            self.who = "Elizabeth"

    def __repr__(self):
        msg="""
        {who}'s check. ${amount}, {date}, {hours} hours, ${wage}/hr, {gross} gross pay
        """.format(who=self.who, amount=self.amount, date=self.date, hours=self.hours, wage=self.wage, gross=self.gross)
        return msg

