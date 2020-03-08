# Homework task for Week 4
# Write program that asks the user to input any positive integer 
# and output the successive values of the following calculation
# At each step calculate the next value by taking the current value 
# if the current value is even divide it by two 
# but if it is odd multiple by three and add one
# the programme will end if the current value is one

x = int(input("Please enter a positive integer: "))
y = 2
even = False

while (x > 1):
    if (x % y) == 0:
        even = True
    else:
        even = False
    if even:
        x = int(x / 2)
    else:
        x = int(x * 3 + 1)
    print(x)


    
 