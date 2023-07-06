import random

class Hangman():
    '''
    A hangman game
    
    '''
    def __init__(self, word_list, num_lives=5):
        '''
        __init__()
            init(word_list, num_lives)
        
        Initializes the class

        word: The word to be guessed, picked randomly from the word_list. Remember to import the random module into your script.
        word_guessed: list - A list of the letters of the word, with for each letter not yet guessed. For example, if the word is 
        'apple', the word_guessed list would be ['', '', '', '', '']. If the player guesses 'a', the list would be ['a', '', '', '', ''].
        num_letters: int - The number of UNIQUE letters in the word that have not been guessed yet.
        num_lives: int - The number of lives the player has at the start of the game.
        word_list: list - A list of words.
        list_of_guesses: list - A list of the guesses that have already been tried. Set this to an empty list initially
        '''
        self.word_list = word_list
        self.word = random.choice(self.word_list)
        self.word_guessed = ['_' for letter in self.word]
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.list_of_guesses = []

    def check_guess(self, guess):
        '''
        Check if the guess is in the word

        check_guess()
            check_guess(guess)
        
        guess String Contains a word
        '''
        guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            # replace _ with letter in word_guessed for each instance of the letter
            for index in range(0, len(self.word)):
                if self.word[index] == guess:
                    self.word_guessed[index] = guess
            self.num_letters -= 1    
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")
        print(myhangmangame.word_guessed)
                
    def ask_for_input(self):
        '''
        ask the user to guess a letter
        
        ask_for_input()
            ask_for_input()

        '''
        while True:
            guess = input('Please input a single letter: ')
            if len(guess) != 1 or not guess.isalpha():
                print('Invalid Letter. Please, enter a single alphabetical character.')
            elif guess in self.list_of_guesses:
                print('You already tried that letter')
            else:
                self.check_guess(guess)
            self.list_of_guesses.append(guess)


word_list = ['banana','apple','pear', 'persimmon','mango']
myhangmangame = Hangman(word_list)
myhangmangame.ask_for_input()



