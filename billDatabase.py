# initialize bills here
# this is the current database, eventually maybe I'll replace this with a GUI but for now this works fine as I am the only intended user

from BillsClass import *
from decimal import *

getcontext().prec = 2

# rent = Bill(name, cost, dueDate, billType, gracePeriod, interestRate, notes)
rent = Bill("Rent", 1250, 1, "Rent", 7, 0, "Due date is flexible")
carPayment = Bill("Car Payment", 332.79, 28, "Car Loan", 7, 5.36)
carInsurance = Bill("Car Insurance", 178.05, 2, "Insurance", 9, 0, "Can be delayed to the 11th, but has to be done a few days before")

