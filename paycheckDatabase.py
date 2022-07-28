# initialize paycheck objects here
# this is the current database, eventually maybe I'll replace this with a GUI but for now this works fine as I am the only intended user

from PaycheckClass import *

# RECORD BILLS HERE
joeCheck1 = PayCheck(True, 614.87, "7/28/22" ,12+31.50+1, 17, 756.50)


print(joeCheck1)