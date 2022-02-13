from game.rand_word import Word
from game.terminal_service import TerminalService
from game.parachute_display import ParachuteMan

class Director:
    """A person who directs the game. 

    The responsibility of a Director is to control the sequence of play.

    Attributes:
        random word: The word the user has to guess.
        is_playing (boolean): Whether or not to keep playing.
        parachute: The parachute man display.
        terminal_service: For getting and displaying information on the terminal.
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self._word = Word()
        self._is_playing = 'yes'
        self._parachute = ParachuteMan()
        self._terminal_service = TerminalService()
        
    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self._is_playing == 'yes':
            self._get_inputs()
            self._do_updates()
            self._do_outputs()

    def _get_inputs(self):
        """gets the users guess.

        Args:
            self (Director): An instance of Director.
        """
        self._word.get_letter()
        
    def _do_updates(self):
        """Keeps count of the users guesses and decides if they are correct.

        Args:
            self (Director): An instance of Director.
        """
        self._parachute.check_word(self._word)
        self._parachute.check_win(self._word)
        
        
    def _do_outputs(self):
        """Shows the user what they have guessed correctly and updates the parachute display.
           If they have won or lost display a message and end the game.
        Args:
            self (Director): An instance of Director.
        """
        self._parachute.show()
        self._word.guess_lines()
        if self._parachute._won == 'yes':
            self._terminal_service.write_text("\nCongratulations you won!")
            self._is_playing = 'no'
            
        elif self._parachute._lose == 'yes':
            self._terminal_service.write_text("\nYou Lose!")
            self._is_playing = 'no'


