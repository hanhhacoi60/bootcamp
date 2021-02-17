# This is the basic rock paper scissors project for The Modern Python3 Bootcamp

print("Welcome to the most boring game of Rock, Paper, Scissors ever created!")

player_1 = input("Hello, Player 1! Choose rock, paper, or scissors:     ")

for i in range(50):
	print("NO CHEATING!")

player_2 = input("Hello, Player 2! Choose rock, paper, or scissors:     ")

print("SHOOT!")

if player_1 != "rock" and player_1 != "scissors" and player_1 != "paper":
	print("Something went wrong! :(")
elif player_2 != "rock" and player_2 != "scissors" and player_2 != "paper":
	print("Something went wrong! :(")
elif player_1 == player_2:
	print("IT'S A TIE")	
	print("Good game!")
elif player_1 == "rock":
	if player_2 == "scissors":
		print("Player 1 WINS by crushing the scissors with rock!")
	else:
		print("Player 2 WINS by covering the rock with paper!")
	print("Good game!")
elif player_1 == "scissors":
	if player_2 == "rock":
		print("Player 2 WINS by crushing the scissors with rock!")
	else:
		print("Player 1 WINS by cutting the paper with scissors!")
	print("Good game!")
elif player_1 == "paper":
	if player_2 == "rock":
			print("Player 1 WINS by covering the rock with paper!")
	else: 
			print("Player 2 WINS by cutting the paper with scissors!")
	print("Good game!")
else: 
	print("Something went wrong :( ")





## Below is my first version, where the ties are not separated out



# if player_1 == "rock":
# 	if player_2 == "rock":
# 		print("It's a tie! How boring!")
# 	elif player_2 == "scissors":
# 		print("Player 1 WINS by crushing the scissors with rock!")
# 	else:
# 		print("Player 2 WINS by covering the rock with paper!")
# elif player_1 == "scissors":
# 	if player_2 == "scissors":
# 		print("It's a tie! How boring!")
# 	elif player_2 == "rock":
# 		print("Player 2 WINS by crushing the scissors with rock!")
# 	else:
# 		print("Player 1 WINS by cutting the paper with scissors!")

# elif player_1 == "paper":
# 	if player_2 == "paper":
# 		print("It's a tie! How boring!")
# 	elif player_2 == "rock":
# 		print("Player 1 WINS by covering the rock with paper!")
# 	else: 
# 		print("Player 2 WINS by cutting the paper with scissors!")
# else:
# 	print("Something went wrong!")
# print("Good game!")