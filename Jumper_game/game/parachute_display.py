import random
from game.rand_word import Word
from game.parachutes import parachute


class ParachuteMan:
    """Constructs a new instance of jumper.
    the logic is to choose which picture gets will be displayed.
    If they get a correct letter or a wrong one.
    Args:
        self(jumper): An instance of jumper.
        """
    def __init__(self):
        self.guess = ""
        self.attempt = 0
        self.won = 'no'
        self.lose = 'no'

    def check_word(self, word):
        """Checks the random word to see is the letter guessed by the user is in the word."""
        if word.user_guess in word.word:
                self.guess = 'correct'
        else:
            self.attempt += 1
            self.guess = 'incorrect'
            if self.attempt == 4:
                self.lose = 'yes'

    def check_win(self, word):
        if word.word == word.blanks:
            self.won = 'yes'

    def show(self):
        """prints out the picture and uses the logic needed to change depending on the number of attemp count."""
        print(parachute[self.attempt])
        print(f'That\'s {self.guess}!')

