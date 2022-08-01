# initialize bills here
# this is the current database, eventually maybe I'll replace this with a GUI but for now this works fine as I am the only intended user

from BillsClass import *
from decimal import *

getcontext().prec = 2

# rent = Bill(name, cost, dueDate, billType, gracePeriod, interestRate, notes)
rent = Bill("Rent", 1250, 1, "Rent", 7, 0, "Due date is flexible")

wellsFargo = Bill("Wells Fargo Card", 37, 2, "Credit Card", 0, 0, "interest rate unknown")

EpayPal = Bill("Elizabeth's PayPal Card", 71, 2, "Credit Card", 7, 0, "interest rate unknown")

carInsurance = Bill("Car Insurance", 178.05, 2, "Insurance", 9, 0, "Can be delayed to the 11th, but has to be done a few days before")

spotify = Bill("Spotify", 12.99, 4, "Streaming", 31, 0)

capitalOne = Bill("Capital One Card 1", 25, 4, "Credit Card", 0, 0, "interest rate unknown")

rentersInsurance = Bill("Renters Insurance", 18.42, 5, "Insurance", 9, 0)

adobe = Bill("Adobe Suite", 29.99, 6, "Tools", 31, 0, "Limited time discount")

rings = Bill("Ring Credit Card", 25, 8, "Credit Card", 0, 0, "interest rate unknown, approx 190 owed")

internet = Bill("Ziply Internet", 53.19, 10, "Utility", 0, 0, "grace period unknown")

washer = Bill("Home Depot Card", 34, 11, "Credit Card", 0, 0, "interest rate unknown, washer is being paid down")

affirmIT1 = Bill("Affirm A+ Exam Pt.1", 22.62, 12, "Credit Card", 0, 290.99, "Paid off November 2022")

capitalTwo = Bill("Capital One Card 2", 25, 12, "Credit Card", 0, 0, "interest rate unknown")

affirmIT2 = Bill("Affirm A+ Exam Pt.2", 23.30, 13, "Credit Card", 0, 29.99, "Paid off January 2023")

EcareCredit = Bill("Elizabeth's Care Credit", 0, 13, "Credit Card", 0, 0, "interest rate unknown, Ends Jan 2023, parents pay")

destinyCard = Bill("Destiny Card", 40, 13, "Credit Card", 0, 0, "interest rate unknown")

trash = Bill("Trash", 34.72, 15, "Utility", 0, 0, "Grace period unknown")

EchaseCard = Bill("Elizabeth's Chase Card", 40, 15, "Credit Card", 0, 0, "interest rate unknown")

JcareCredit = Bill("Joe's Care Credit", 29, 16, "Credit Card", 0, 0, "interest rate unknown")

creditOne = Bill("Elizabeth's Credit One Card", 30, 16, "Credit Card", 0, 0, "interest rate unknown")

JpayPal = Bill("Joe's PayPal Card", 64, 16, "Credit Card",  0, 0, "interest rate unknown, grace period unknown")

Jupstart = Bill("Joe's Upstart", 194.54, 17, "Upstart", 15, 23.20)

verizon = Bill("Verizon", 113.53, 18, "Utility", 0, 0)

fortivaCard = Bill("Joe's Fortiva Card", 59, 18, "Credit Card", 0, 0, "interest rate unknown")

Eupstart = Bill("Elizabeth's Upstart", 213.05, 19, "Upstart", 15, 0, "interest rate unknown")

powerBill = Bill("Pacific Power", 105, 20, "Utility", 15, 0, "Changes monthly due to usage")

googleDrive = Bill("Google Drive", 9.99, 20, "Tools", 31, 0)

disneyPlus = Bill("Disney Plus", 7.99, 27, "Streaming", 31, 0)

EcarInsurance = Bill("Elizabeth's Car Insurance", 0, 27, "Insurance", 9, 0, "Parents pay")

xbox = Bill("Xbox Payments", 35, 28, "Credit Card", 0, 0, "interest rate unknown")

carPayment = Bill("Car Payment", 332.79, 28, "Car Loan", 7, 5.36)

backTaxes = Bill("Back Taxes from 2021", 35, 28, "Tax Debt", 0, 0)

gas = Bill("Gasoline Estimate", 150, 31, "Utility", 31, 0, "Needs to be properly calculated")

food = Bill("Food Estimate", 300, 31, "Utility", 31, 0, "Needs to be properly calculated")


