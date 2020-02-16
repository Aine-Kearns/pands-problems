# this programme reads	in	a	string	and	strips	any	
# leading	or	trailing	spaces
# it also	converts	the	string	to	
# lower	case and 	also	outputs	the	length	of	the	input	and	
# output	strings

rawString = input("Please enter a string: ")

normalisedString = rawString.strip().lower()

lengthofRawString = len(rawString)
lengthofNormalisedString = len(normalisedString)

print("That String normalised is: {}".format(normalisedString))
print("We reduced the input string from {} to {} characters".format(lengthofRawString, lengthofNormalisedString))