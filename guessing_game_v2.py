# This is Colt's Answer, which is more succinct than what I got on my own
import random

random_number = random.randint(1, 10)

while True:
	guess = input("Pick a number from 1 to 10: ")
	guess = int(guess)

	if guess < random_number:
		print(f"Your guess of {guess} was TOO LOW!")
	elif guess > random_number:
		print(f"Your guess of {guess} was TOO HIGH!")
	else:
		print(f"Your guess of {guess} was CORRECT!!")
		play_again = input("Do you want to play again? (y/n): ")
		if play_again == "y":
			random_number = random.randint(1, 10)
		else:
			print("Thanks for playing!")
			break