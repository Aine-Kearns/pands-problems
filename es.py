# Homework for week 7
# Write a program that reads in a text file - taken from https://www.gutenberg.org/files/2701/old/moby10b.txt
# then outputs the numbers of e's the file contains

with open("moby-dick.txt", "r") as f:
    # open text file
    x = f.read()
    # need to change f which is classed as an IO to string so I can use count 
    # found a bit about count on https://www.guru99.com/python-string-count.html
    howmanye = x.count("e")
    # count the lower case e
    howmanyE = x.count("E")
    # count upper case e
    print(howmanye + howmanyE)
    # print total count of upper and lower case 