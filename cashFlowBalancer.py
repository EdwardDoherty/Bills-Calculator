# Game Plan:
# Take total cost in given range (default 4 weeks)

# Figure out how many paychecks occur during that range

# Ask for expected paycheck Net income, but default to paycheck Defaults supplied in paycheckDatabase.py

# Calculate how much each paycheck is as a percentage of total income for the range

# Take those percentages and apply them to the total costs for the range,
# So if paycheck 1 is 25% of the income during the selected period, then calculate 25% of the total cost and apply it to that paycheck

# Add the remainder to a "Remainder" variable, we can use this to calculate savings goals in the future

# We should now have a perfectly balanced cash flow

from functions import *


def cashFlowBalancer():
    pass