# Homework task for Week 4
# Write program that asks the user to input any positive integer 
# and output the successive values of the following calculation
# At each step calculate the next value by taking the current value 
# if the current value is even divide it by two 
# but if it is odd multiple by three and add one
# the programme will end if the current value is one

x = int(input("Please enter a positive integer: "))
y = 2

while (y < x):
    if (y % x) == 0:
        print(x / 2)
    else:
        print(x * 3 )
y = 1

