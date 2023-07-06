Hangman Milestone_2.py 

I Set up the environment

I built the basic code
    if... else
    functions
    lists
    command line interaction


Created functions store the code
    ask_for_input()
    check_guess(guess)
        guess - alpha 1

The Hangman class instantiates with a supplied list of words. It picks one and sets up internal variables. 

The function ask_for_input is run to start the game. This asks for a letter and checks that it is valid. 
If it is okay then if calls check_guess to see whether the letter is in the chosen word, otherwise it asks for valid letter.
check_guess looks to see whether the guess is in the word and if it is then it updates the internal variables. Messages are printed to the terminal to feedback to the user. 

The game is run from outside using a function Play_the_game. This calls ask_for_input and checks whether the game is over. 
I was expecting this to be a static method, but I see from StackOverflow that static methods should only be used sparingly. It seems odd to me because it leaves the running code outside the class.


