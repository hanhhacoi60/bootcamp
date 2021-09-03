def dad_joke():
    """
    Asks user for category of joke. Returns a random joke from
    https://icanhazdadjoke.com/ within that category. If there no joke
    exists in that category, asks user for another category.
    """
    # IMPORTS
    import requests
    from pyfiglet import figlet_format
    from termcolor import colored
    from random import choice

    # INTRO TO GAME
    intro_message = "Welcome to Dad Joke 3000!"
    print(
        colored(
            figlet_format(intro_message, font='standard'),
            color="cyan"
        )
    )
    # ESTABLISHES COUNTER FOR MULTIPLE ROUNDS
    counter = 0

    # HTTP REQUEST
    while counter == 0:
        category = input("Let me tell you a joke! Give me a topic: ")

        url = "https://icanhazdadjoke.com/search"

        response = requests.get(
            url,
            headers={"Accept": "application/json"},
            params={"term": category}
        )

        data = response.json()
        jokes = data["results"]

    # DETERMINE RESPONSE
        if len(jokes) < 1:
            print(
                f"Sorry, I don't have any jokes about {category}! Please try again."
            )
        else:
            if len(jokes) > 1:
                print(
                    f"I have {len(jokes)} jokes about {category}. Here's one: "
                )
                rand_joke = choice(jokes)
                print(rand_joke["joke"])
            else:
                print(f"I have one joke about {category}. Here it is: ")
                print(jokes[0]["joke"])

    # ASKING IF PLAYER WANTS TO PLAY AGAIN
            another = input(
                "Would you like to hear another joke? Type 'Y' or 'N'.: ")

            while another != 'Y' and another != 'N':
                another = input(
                    "Sorry, please try again. Type in 'Y' or 'N'.: ")
            if another == 'Y':
                counter = 0
            else:
                print("Ok, thanks for playing!")
                counter = 1


def main():
    """
    runs dad_joke()
    """
    dad_joke()


main()
