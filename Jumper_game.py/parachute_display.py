#this file handles the parachute man display
#and the score of the game or life count
import random
from rand_word import word
from jump_main import parachute


class ParachuteMan:
    """Constructs a new instance of jumper.
    the logic is to choose which picture gets will be displayed.
    If they get a correct letter or a wrong one.
    Args:
        self(jumper): An instance of jumper.
        """
    def __init__(self):
      self.word = word
      self.guess = ""
      self.reveal = list(len(self.word)*'_')
      self.attemp = 4
      self.won = False
      self.lose = False

    def check_word(self, letter, word):
      """Checks the random word to see is the letter guessed by the user is in the word."""

      for i in range(0,len(self.word)):
          letter = self.word[i]
          if self.guess == letter:
              self.reveal[i] = self.guess
      if '_' not in self.reveal:
          return True
      else:
          return False


    def show(self):
      """prints out the picture and uses the logic needed to change depending on the number of attemp count."""
      print(parachute[4 - self.attemp])
      print(self.reveal)
    def process(self):
      """This is the logic while trying to get the guessing game to work
      It checks the letter"""
      while self.won == False and self.attemp > 0:
          self.show()
          self.guess = input('guess a letter from[a-z]: ')
          self.guess = self.guess.upper()
          
          """if the guess letters are equal to the word than they won!"""
          if self.guess == self.word:
              self.won = True
              self.reaveal = self.word
              """if the user guess well one letter from the word this mean he does not win"""
          if len(self.guess) == 1 and self.guess in self.word:
              self.won = self.letter_check(self.guess, self.word)   
          else:
              self.attemp-=1
          """When win is official this prints Congratulations message"""
          if self.won == True:
              print(f"Well done! you guessed {self.word}")
              print("")
          else:
              print("sorry, you lose")
              print(" ")
          """When loss is confirmed this prints the last picture"""
          if self.attempt == 0:
              self.lose = True
          if self.lose == True:
              print(parachute[4])
              print("You've lost")
              self.lost = False
              print(self.word)
