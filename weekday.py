# Homework Week 5
# Develop a program that outputs whether or not today is a weekday

import datetime
# import date and time dictionary - taken from https://www.w3schools.com/python/python_datetime.asp
now = datetime.datetime.now()
# find out the day with Monday starting at 0
now.weekday()

# weekday = [0, 1, 2, 3, 4]  this is based on the knowledge that Monday starts at 0 as noted above
# weekend = [5, 6]

if now.weekday()<=4:
    # used the knowledge that 0 - 4 is a weekday and 5 - 6 is the weekend 
    print("Yes, unfortunately today is a weekday.")
else:
    print("It's the weekend, yay!")
   



# Yes, unfortunately today is a weekday.
# It's the weekend, yay!