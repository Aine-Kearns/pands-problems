# a program that reads in a text file
# then outputs the numbers of e's the file contains

with open("moby-dick.txt", "r") as f:
    x = f.read()
    howmanye = x.count("e")
    howmanyE = x.count("E")
    print(howmanye + howmanyE)