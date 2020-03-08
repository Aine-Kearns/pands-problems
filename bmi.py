#Programme to calculate BMI

#height in centimetres
#weight in kilograms

height = float(input("Enter height in centimeters: "))
weight = float(input("Enter weight in kilograms: "))

h = (height/100)**2
BMI = weight/h

print("Body Mass Index is", round(BMI,2))