
# Creates a list of jobs
# When creating jobs follow THIS format:
# jobname = Job(name, wage, payFreq, avgHours, deductions, isJoes, notes)
from JobClass import *

#initiate jobs here. DO NOT DELETE ANYTHING UNLESS YOU KNOW WHAT YOU ARE DOING
#We want to save this info
homeDepot = Job("Home Depot", 17, 14, 40, True, 16, "Home Depot as of July 30th 2022")
earlyHeadstart = Job("Early Head Start", 18.69, 14, 80, False, 40, "Early Head Start as of July 30th 2020")



JcurrentJob = homeDepot
EcurrentJob = earlyHeadstart 