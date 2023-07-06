import random
word_list = ['banana','apple','pear', 'persimmon','mango']
word = random.choice(word_list)
print(word)

def check_guess(guess):
    '''
    check_guess(...)
        check_guess(guess)

    Checks whether a string is alpha and single character
    guess: a string
    '''
    guess.lower()
    if guess in word:
        print(f'Good guess! {guess}')
    else:
        print(f'Sorry, {guess} is not the word. Try again')

def ask_for_input():
    '''
    ask_for_input()
        ask_for_input()

    Asks the user for input and validates it and checks whether it is in the chosen word
    '''
    while True:
        guess = input('Please input a single letter: ')
        if len(guess) == 1 and guess.isalpha():
            break
        else: 
            print('Invalid Letter. Please, enter a single alphabetical character.')
    check_guess(guess)

#ask_for_input()


help(ask_for_input)