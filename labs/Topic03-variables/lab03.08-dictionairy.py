# create dictionary item
currentBook = {
    "title" : "Harry Potter eats his dinner",
    "author" : "Just Kidding Rowling",
    "price" : 12
}
# print dictionary object
print (currentBook)
# print just the author
print (currentBook["author"])
# create and set attibute ISBN
currentBook["ISBN"] = "12345"

# user for loop to iterate through the currentBook's values 
# notice the order the loop gives the values
print ("the current book has these values:")
for value in currentBook.values():
    print (" =>{}".format(value))