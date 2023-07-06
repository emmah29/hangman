import random
word_list = ['banana','apple','pear', 'persimmon','mango']
print(','.join(word_list))

word = random.choice(word_list)
print(word)

guess = input('Please input a single letter: ')
print(guess)

if len(guess) == 1 and guess.isalpha():
    print('Good guess!')
else: 
    print('Oops! That is not a valid input')

