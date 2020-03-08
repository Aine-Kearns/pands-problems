# Homework Week 5
# Develop a program that outputs whether or not today is a weekday

import datetime
# import date and time dictionary
now = datetime.datetime.now()
# find out the day with Monday starting at 0
now.weekday()

#weekday = [0, 1, 2, 3, 4]
#weekend = [5, 6]

if now.weekday()<=4:
    # used the knowledge that 0 - 4 is a weekday and 5 - 6 is the weekend 
    print("Yes, unfortunately today is a weekday.")
else:
    print("It's the weekend, yay!")
   



# Yes, unfortunately today is a weekday.
# It's the weekend, yay!