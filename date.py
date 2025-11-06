import time
import datetime
print("Current Date & Time :",datetime.datetime.now())
print("Current Year :",datetime.date.today().strftime("%Y"))
print("Current  Month of Year :",datetime.date.today().strftime("%B"))
print("Week number of Year:",datetime.date.today().strftime("%W"))
print("Day number of Week :",datetime.date.today().strftime("%W"))
print("Day  of Year :",datetime.date.today().strftime("%j"))
print("Day of The Month  :",datetime.date.today().strftime("%d"))
print("Day  of Week :",datetime.date.today().strftime("%A"))
print("\n Using time module :")
current_time = time.localtime()
print("Today's date : ",time.strftime("%Y-%m-%d",current_time))