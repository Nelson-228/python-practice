# Creating a variable with an integer value
number = 5

# Creating a variable with a string value
text = "Hello World"

# An argument is between the opening & closing parentheses & "print()" displays a message for what ever is inside the parentheses
print()

# For example, the argument inside print(), is the variable "text", which should display "Hello World".
print(text)

# Each string character has its own numerical index, for example... "H" is [0], "e" is [1], and so on..
print("Hello World")

# I want to print out only the "W" in the "text" variable. To do that, we must do this..
print(text[6])

# You can also access string characters with a negative number. However, instead of the first number starting at 0, it starts off at the last string index with -1. For example...
print(text[-1]) # It should print "d", since it is the last string index of the text

# What if you want to see how many # of characters are in the string? Well, you can use the len() function! Here is an example!
print(len(text)) # Since there are 11 characters in the "text" variable, it should print 11.

# However, how can I know what data type is the variable? We can use the type() function to figure that out! Here is an example!
print(type(text)) # Since it is a string, it will print it as "str".

shift = 3

# Finished with Phase 0, Day 1 of SWE Study!!
