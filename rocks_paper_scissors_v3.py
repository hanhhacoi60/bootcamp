
print("Welcome to Rocks, Paper, Scissors Version 2: Computer Edition!!!!")


from random import choice

player_wins = 0
computer_wins = 0

while player_wins < 2 and computer_wins < 2:
    print(f"Player Score: {player_wins} Computer Score: {computer_wins}")

    human_player = input("Hello, human. Make your move:   ")
    if human_player == "quit" or input == "q":
        break

    choices = ["rock", "paper", "scissors"]

    computer_player = choice(choices)

    print(f"You have chosen {human_player}. I have chosen {computer_player}")

    if human_player == computer_player:
        print("IT'S A TIE")

    elif human_player == "rock":
        if computer_player == "scissors":
            print("NOOO, YOU'VE BEAT ME HUMAN")
            player_wins += 1
        else:
            print("I'VE WON. I WILL CONTINUE TO BE YOUR OVERLORD.")
            computer_wins += 1

    elif human_player == "scissors":
        if computer_player == "rock":
            print("I'VE WON. I WILL CONTINUE TO BE YOUR OVERLORD.")
            computer_wins += 1
        else:
            print("NOOO, YOU'VE BEAT ME HUMAN")
            player_wins += 1

    elif human_player == "paper":
        if computer_player == "rock":
            print("NOOO, YOU'VE BEAT ME HUMAN")
            player_wins += 1
        else:
            print("I'VE WON. I WILL CONTINUE TO BE YOUR OVERLORD.")
            computer_wins += 1

print(f"FINAL SCORES: Player: {player_wins} Computer {computer_wins}")
if player_wins > computer_wins:
    print("Congratulations, Player. You WON")
elif player_wins == computer_wins:
    print("It's a tie!")
else:
    print("Sorry, Player. You lost :(")
