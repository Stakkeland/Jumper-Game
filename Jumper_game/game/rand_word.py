import random

class Word:
    '''The object of the class word is to pick a random word and check to see if inputed letter is in random word '''

    def __init__(self):
        '''creates a new word and gets length '''

        self.words = ["python", "cheese", "jello", "easy", "hawks", "long", "common", "difficult"]
        self.word = random.choices(self.words)[0]
        self.len = len(self.word)
        self.blanks = '_' * self.len
        self.user_guess = ''

    def get_letter(self):
        '''Gets input for a guessed letter from user'''
        
        self.user_guess = input('Guess a letter [a-z]: ').lower()
        return self.user_guess

    def guess_lines(self):
        '''creates lines to show length of word with letters filled out as game progresses'''

        
        for i in range(self.len):
            if self.user_guess in self.word[i]:
                self.blanks = self.blanks[:i] + self.word[i] + self.blanks[i+1:]

        for letter in self.blanks:
            print(letter, end=' ')
