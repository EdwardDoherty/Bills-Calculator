
# creates the Paycheck() class, which keeps track of
# Whos check it was
# Net revenue. Take home pay
# Date money was received
# Hours you worked this paycheck
# Your hourly wage at this time
# Gross pay, before taxes and deductions



class PayCheck:

    def __init__(self, amount, date=None, hours=None, job=None, notes=None):
        self.amount = amount
        self.date = date
        self.hours = hours
        self.job = job
        self.notes = notes


    def __repr__(self):
        msg="""
        {who}'s check. ${amount}, {date}, {hours} hours, {job}. Notes:"{notes}"
        """.format(who=self.job.who, amount=self.amount, date=self.date, hours=self.hours, job=self.job.name, notes=self.notes)
        return msg


