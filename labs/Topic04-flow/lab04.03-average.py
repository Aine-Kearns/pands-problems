# This programme reads in numbers until
# the user enters 0
# it will then print back out the numbers again
# and their average

numbers = []

# first number then we check it if is 0 in the while loop

number = int(input("Enter number (0 to quit): "))

while number != 0:
    numbers.append(number)

    # read the next number and check if 0
    number = int(input("enter another (0 to quit): "))

for value in numbers:
    print (value)

# I want average to be a float

average = float(sum(numbers)) / len(numbers)
print ("The average is {}". format(average))
