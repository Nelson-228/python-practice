# Modifying the below code to display data type of the variables
text = "Hello World"
print(type(text)) # Data type of text is string (str)
shift = 3
print(type(shift)) # Data type of shift is integer (int)

# Removing the prnt function and adding another variable for "alphabet"
text = 'Hello World'
alphabet = "abcdefghijklmnopqrstuvwxyz"
shift = 3

# Using a new function, .find(), returns the requested letter or number from its index.
text = 'Hello World'
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphabet.find("z")

# We will modify the .find() function into finding the first letter in the variable "text" which is "H" in the variable "alphabet".
# However, notice that none of the letters are capitalized in the variable, "alphabet". So, we will be using .lower() in order to return the string lowercase.
text = 'Hello World'
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphabet.find(text[0].lower())

# We are only assigning the alphebet.find(text[0]) variable to another variable called "index" to make it easier for us to use.
text = 'Hello World'
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'
index = alphabet.find(text[0].lower())

# Printing the output of "index"
text = 'Hello World'
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'
index = alphabet.find(text[0].lower())
print(index) # Output is 7 for "h" in alphabet is in index # 7

# Example of .lower() use
text = 'Hello World'
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'
index = alphabet.find(text[0])
print(index)
print(text.lower()) # This will print out "text" all in lower case

# We are creating a new variable called "shifted" to display the index number instead of each character in the variable "alphabet"
text = 'Hello World'
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'
index = alphabet.find(text[0].lower())
print(index)
shifted = alphabet[index] # So, instead of "a", it will now be assigned [0]. Also its output will be "7" because the character "h" is display in index # 7.
