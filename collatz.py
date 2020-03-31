# Homework task for Week 4
# Write program that asks the user to input any positive integer 
# and output the successive values of the following calculation
# At each step calculate the next value by taking the current value 
# if the current value is even divide it by two 
# but if it is odd multiple by three and add one
# the programme will end if the current value is one

x = int(input("Please enter a positive integer: "))
# allow the user to input a positive integer number
y = 2
# need this for calculation later


while (x > 1):
    # this will continue to run through the loop in the programme only once x is a positive number greater than one
    if (x % y) == 0:
        # this means there is no remainder so it is an even number and therefore even is true
        x = int(x / 2)
    else:
        # if the number is odd it will be multiplied by three and one will be added
        x = int(x * 3 + 1)
    print(x)


    
 