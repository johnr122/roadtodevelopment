"""
--------------------------------
Project 1 - Number Guessing Game
--------------------------------
"""

from random import *


def start_game():
    """Psuedo-code Hints
    
    When the program starts, we want to:
    ------------------------------------
    1. Display an intro/welcome message to the player.
	2. Store a random number as the answer/solution.
    3. Continuously prompt the player for a guess.
      a. If the guess greater than the solution, display to the player "It's lower".
      b. If the guess is less than the solution, display to the player "It's higher".
    
    4. Once the guess is correct, stop looping, inform the user they "Got it"
         and show how many attempts it took them to get the correct number.
    5. Let the player know the game is ending, or something that indicates the game is over.
    
    ( You can add more features/enhancements if you'd like to. )
    """
    # write your code inside this function.
    name = input("Hello, What's your name? ")
    print("\n"+"-"*40)
    print("Welcome to the Number Guessing Game {}.".format(name))
    print("-"*40,"\n")
    highscore = []
    while True:
        
        answer = randint(1,10)
        guess = ""
        x = 0
        while answer != guess:
            guess = int(input("Pick a number between 1 to 10: "))
            x += 1
            if answer > guess and 10>= guess > 0:
                print("It is higher.")
            elif answer < guess and 10>= guess > 0:
                print("It is lower.")
            else:
                print("Answer must only be between 1 and 10")
            continue
        print("")
        highscore.append(str(x))
        highscore.sort()
        
        if x == 1:
            print("Nice! You got it on your first try!.")
        else:
            print("You got it! It took you {} tries.\n\n".format(x))
        try_again = input("Do you want to try again? yes/no: ")
        print("-"*40)
        
        if try_again.lower() == 'yes':
            print("The highscore is {} try/tries." .format(highscore[0]))
            print("-"*40)
            continue
        elif try_again.lower() == 'no':
            print("Thank you.")
            break
        else:
            print("You didn't even answer yes or no.. T_T")
            print("Thank you anyways")
            break
        
        
if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    start_game()
