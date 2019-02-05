# -*- coding: utf-8 -*-

# Initializing Variables
welcome_message = 'Good Morning! Welcome to Varun Academy.'
lastname = firstname = gender = name = wait_message = ''

# Printing Welcom Message
print(welcome_message)

# Taking Inputs
lastname = input("May I know your Last Name?")
firstname = input("May I know your First Name?")
gender = input("May I know your Gender Please?")
name = input("Whom do you want to Meet?")

# Printing the wait message
wait_message = "Hello Mr. {1} {0}, Mr. {3} will meet you in 5 minutes. Request you to take a seat and have a cup of coffee.".format(firstname, lastname, name)

print(wait_message)

