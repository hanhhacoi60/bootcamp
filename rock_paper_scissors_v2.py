print("Welcome to Rocks, Paper, Scissors Version 2: Computer Edition!!!!")

human_player = input("Hello, human. Make your move:   ").lower()

from random import choice

choices = ["rock", "paper","scissors"]

computer_player = choice(choices)
print(f"Hmmm, I see you've chosen {human_player}. \n With all my wisdom, I have chosen: {computer_player} ")

if human_player != "rock" and human_player != "scissors" and human_player != "paper":
	print("Something went wrong! :(")

elif human_player == computer_player:
	print("IT'S A TIE")	
	print("Good game, human! But you are still not equal to me!")

elif human_player == "rock":
	if computer_player == "scissors":
		print("NOOO, YOU'VE BEAT ME HUMAN")
	else:
		print("I'VE WON. I WILL CONTINUE TO BE YOUR OVERLORD.")

elif human_player == "scissors":
	if computer_player == "rock":
		print("I'VE WON. I WILL CONTINUE TO BE YOUR OVERLORD.")
	else:
		print("NOOO, YOU'VE BEAT ME HUMAN")

elif human_player == "paper":
	if computer_player == "rock":
			print("NOOO, YOU'VE BEAT ME HUMAN")
	else: 
			print("I'VE WON. I WILL CONTINUE TO BE YOUR OVERLORD.")

else: 
	print("Please enter a valid move.")

