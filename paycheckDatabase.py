# initialize paycheck objects here
# this is the current database, eventually maybe I'll replace this with a GUI but for now this works fine as I am the only intended user

from PaycheckClass import *
from datetime import *

joeWage = 17
joeHours = 40

elizWage = 18.69
elizHours = 80

joeDefaultCheck = PayCheck(True, 550, "DEFAULT", joeHours, joeWage, joeWage*joeHours, "DEFAULT CHECK")
ElizDefaultCheck = PayCheck(False, 1130, "DEFAULT", elizHours, elizWage, elizWage*elizHours, "DEFAULT CHECK")

# RECORD BILLS HERE
# ALWAYS REMEMBER TO RECORD DATE AS SHOWN BELOW, YEAR, MONTH, DATE
joeCheck1 = PayCheck(True, 614.87, date(2022,7,28), 12+31.50+1, 17, 756.50, "First check entered into this program")


print(joeCheck1)
print(joeDefaultCheck)
print(ElizDefaultCheck)