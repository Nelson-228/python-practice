password = "OpenSesame"

UsersGuess = input("Enter password: ")

while UsersGuess != password: # While User guessed does not equal password, it will keep the user on the loop until the password is correct
    UsersGuess = input("Incorrect Try again \nEnter Password: ")

print("Access Granted") # Will only print until user escapes the "while" loop by getting the password correct

