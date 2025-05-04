"""
password_checker.py
--------------------
A simple password authentication loop.

- Prompts the user for a password.
- Repeats the prompt until the correct password is entered.
- Demonstrates use of `while` loops and conditional logic.

Purpose: Practice using input validation and loops in Python.

"""

password = "OpenSesame"

UsersGuess = input("Enter password: ")

while UsersGuess != password: # While User guessed does not equal password, it will keep the user on the loop until the password is correct
    UsersGuess = input("Incorrect Try again \nEnter Password: ")

print("Access Granted") # Will only print until user escapes the "while" loop by getting the password correct

