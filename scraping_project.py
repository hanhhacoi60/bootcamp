# Quote Guessing Game
# Created 09/17/2021
# Mini project from Colt Steele's Udemy Python class. I created this solution
# on my own, without looking at his answers.

import requests
from bs4 import BeautifulSoup
from time import sleep
from random import choice


class Quote:
    """
    A class to represent a famous Quote.

    **requires requests, bs4 and random modules
    ...

    Public Attributes
    __________
    total_quotes : list
        list of dictionaries of all possible quotes

    chosen_quote: dict
        randomly chosen quote from total_quotes

    Public Methods
    __________
    get_quote(self):
        Returns dictionary of quote text, its author, and the url for the author's biography.

    get_quote_text(self):
        Returns string of quote text.

    get_quote_author(self):
        Returns string of quote's author.

    get_quote_url(self):
        Returns string of url for the author's biography. Use as:
        http://quotes.toscrape.com/page/{get_quote_url()}

    def get_total_quotes(self):
        Returns list of all possible quotes scraped from http://quotes.toscrape.com.

    """

    def __init__(self):
        """
        Instantiates a Quote object, which comprises a dict with the quote text, the quote's author, and an
        url to the author's bio page.
        """

        self.total_quotes = []
        self._page_num = 1
        self._next_page = True

        while self._next_page:
            self._page_response = requests.get(
                "http://quotes.toscrape.com/page/{}/".format(self._page_num))
            self._page_soup = BeautifulSoup(
                self._page_response.text, "html.parser")
            self._quotes = self._page_soup.find_all(class_='quote')
            for quote in self._quotes:
                self._text = quote.find(class_='text').get_text()
                self._author = quote.find(class_='author').get_text()
                self._url = url = quote.find('a')['href']
                self._quote_dict = {'Quote': self._text,
                                    'Author': self._author, 'URL': self._url}
                self.total_quotes.append(self._quote_dict)
            self._nav = self._page_soup.find(class_='next')
            if self._nav:
                self._page_num += 1
                sleep(1)
            else:
                self._next_page = False

        self.chosen_quote = choice(self.total_quotes)

    def get_quote(self):
        """Returns dictionary of quote text, its author, and the url for the author's biography."""
        return self.chosen_quote

    def get_quote_text(self):
        """Returns string of quote text."""
        return str(self.chosen_quote['Quote'])

    def get_quote_author(self):
        """Returns string of quote's author."""
        return str(self.chosen_quote['Author'])

    def get_quote_url(self):
        """
        Returns string of url for the author's biography.
        Use as:
        http://quotes.toscrape.com/page/{get_quote_url()}
        """
        return str(self.chosen_quote['URL'])

    def get_total_quotes(self):
        """Returns list of all possible quotes scraped from http://quotes.toscrape.com."""
        return list(self.total_quotes)


def guessing_game(quote):
    """
    Takes a Quote object as its parameter.
    Begins a guessing game in which the player guesses the author of a random quote.
    The player has 4 total guesses. If the player guesses correctly, main() will call
    play_again(). If the player guesses incorrectly, the function automatically calls
    hint(). Letter case and including periods ('.') between initials WILL NOT affect
    the answer.
    """
    print("Welcome to the Quote Guessing Game!\n\nHere's a quote:\n")
    print(quote.get_quote_text())
    print()
    incorrect = True
    global guesses_left
    guesses_left = 4
    while incorrect:
        guess = input(
            f"Who said this?\nGuesses remaining: {guesses_left}.\nYour guess: ")
        global correct_author
        correct_author = quote.get_quote_author()
        correct_author_no_periods = ''.join(correct_author.split('.')).lower()
        guess_no_periods = ''.join(guess.split('.')).lower()

        if guess_no_periods == correct_author_no_periods:
            print("You guessed correctly! Congratulations!")
            incorrect = False
        elif ' ' not in guess.lower():
            print("Please enter the author's first AND last name.")
        else:
            guesses_left -= 1
            print("Sorry, you're incorrect.")
            if guesses_left > 0:
                print("Here's a hint:")
                hint(quote)
            else:
                print("Unfortunately, you've run out of guesses :(")
                print(f"Th÷e correct answer is: {correct_author}")
                incorrect = False


def hint(quote):
    """
    Takes a Quote object as its parameter.
    Prompted if player's initial guess is wrong. Gives up to three hints to the
    player: the author's birthdate and locations of birth, the first letter of the
    author's first name, and the first letter of the author's last name.
    """
    author_list = correct_author.split(' ')
    if guesses_left == 3:
        bio_response = requests.get(
            f"http://quotes.toscrape.com{quote.get_quote_url()}")
        bio_soup = BeautifulSoup(bio_response.text, "html.parser")
        location = bio_soup.find(class_='author-born-location').get_text()
        date = bio_soup.find(class_='author-born-date').get_text()
        hint_1 = f"The author was born {location} on {date}"
        print(hint_1)
    elif guesses_left == 2:
        hint_2 = f"This author's first name begins with: {author_list[0][0]}"
        print(hint_2)
    elif guesses_left == 1:
        if len(author_list) == 2:
            hint_3 = f"This author's last name begins with: {author_list[1][0]}"
        else:
            hint_3 = f"This author's last name begins with: {author_list[2][0]}"
        print(hint_3)


def play_again(quote):
    """
    Takes a Quote object as its parameter.
    Prompted when (1) a player guesses correctly (2) a player has run out of guesses.
    Asks whether the player would like to play again. If so, the main() function is
    called, and a new round beings. If the player answers 'n' or 'no', then the game
    quits. If the player's input is invalid, the prompt will loop until a valid
    input is entered.
    """
    play_again_prompt = True
    while play_again_prompt:
        play = input("Would you like to play again? (y/n):   ")
        if play.lower() == 'y' or play.lower() == 'yes':
            play_again_prompt = False
            main()
        elif play.lower() == 'n' or play.lower() == 'no':
            print("Thanks for playing!")
            play_again_prompt = False
            quit()
        else:
            print("Sorry, I didn't catch that. Please try again.")


def main():
    """
    The main driver code. Saves a new Quote object to the variable 'my_quote', which
    is used to run the quote guessing game.
    """
    my_quote = Quote()
    guessing_game(my_quote)
    play_again(my_quote)


if __name__ == "__main__":
    main()

main()
