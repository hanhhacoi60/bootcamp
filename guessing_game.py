# This is my code that I did without looking at the solution

import random

while True:
	random_number = random.randint(1, 10)
	guess = int(input("Pick a number between 1 and 10: "))

	while guess < random_number:
		print(f"Your guess of {guess} was too low. Try again!")
		guess = int(input())
	while guess > random_number:
		print(f"Your guess of {guess} was too high. Try again!")
		guess = int(input())
	if guess == random_number:
		print(f"Your guess of {guess} was CORRECT!!!")

	print("Would you like to play another game?")

	yes_or_no = input("Type 'y' for 'yes' or 'n' for no: ")

	if yes_or_no == 'y':
		print("Great!")
	elif yes_or_no == 'n': 
		print("Thanks for playing!")
		break
	else:
		print("Oops, something went wrong. ")
		yes_or_no = input("Type 'y' for 'yes' or 'n' for no: ")









