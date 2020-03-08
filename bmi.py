# Homework Week 2
# Programme to calculate BMI

#height in centimetres - should be 180 cm
#weight in kilograms - should be 65 kg

height = float(input("Enter height in centimeters: "))
# using float here to convert the string entered by the user into a floating number
weight = float(input("Enter weight in kilograms: "))

h = (height/100)**2
# need to change from cm to m and square this 
BMI = weight/h
# calculate BMI 

print("Body Mass Index is", round(BMI,2))
#round BMI to 2 decimal places