# This program calculates how many tiles you will need
# when a tiling a wall or floor (in m2).

length = float(input("Enter room length: "))
width = float(input("Enter room width: "))

# length = 3.5
# width = 2.3

area = length * width

needed = area * 1.05

print("You need", needed, "tiles in metre squared.")
