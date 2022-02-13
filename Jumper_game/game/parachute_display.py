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
        self._guess = ""
        self._attempt = 0
        self._won = 'no'
        self._lose = 'no'

    def check_word(self, word):
        """Checks the random word to see is the letter guessed by the user is in the word."""
        if word.user_guess in word.word:
                self._guess = 'correct'
        else:
            self._attempt += 1
            self._guess = 'incorrect'
            if self._attempt == 4:
                self._lose = 'yes'

    def check_win(self, word):
        if word.word == word.blanks:
            self._won = 'yes'

    def show(self):
        """prints out the picture and uses the logic needed to change depending on the number of attemp count."""
        print(parachute[self._attempt])
        print(f'That\'s {self._guess}!')

