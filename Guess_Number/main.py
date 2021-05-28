from random import randint
from art import logo

def easy_level(random_num, name):
    guess_taken = 10
    guess_left = True

    while guess_left:
        # Track the number of turns remaining.
        print(f"You have {guess_taken} attempts remaining to guess the number.")
        guess_taken -= 1
        number = int(input("Take a guess: "))

        if guess_taken > 0 and guess_taken < 11:
            if number < random_num:
                print("Guess is too low. Try Again")
            elif number > random_num:
                print("Guess is too high. Try Again")
            elif number == random_num:
                print(f"Good job {name}, You guessed the correct number.")
                guess_left = False
        else:
            print(f"OOops {name}, You've run out of guesses, You Lose. The correct answer is {random_num}")
            guess_left = False

def hard_level(random_num, name):
    guess_taken = 5
    guess_left = True

    while guess_left:
        print(f"You have {guess_taken} attempts remaining to guess the number.")
        guess_taken -= 1
        # Allow the player to submit a guess for a number between 1 and 100.
        number = int(input("Take a guess: "))

        if guess_taken > 0 and guess_taken < 6:
            # Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
            if number < random_num:
                print("Guess is too low. Try Again")
            elif number > random_num:
                print("Guess is too high. Try Again")
            elif number == random_num:
                print(f"Good job {name}, You guessed the correct number.")
                guess_left = False
        else:
            # If they run out of turns, provide feedback to the player. 
            print(f"OOops {name}, You've run out of guesses, You Lose. The correct answer is {random_num}")
            guess_left = False

def play_game():
    print(logo)
    print("Welcome to Guess The Secret Number Game..")

    num = randint(1, 100)
    print(num)
    name = input("What is Your Name? ").title()
    print(f"Hello {name}, I am thinking of a number between 1 and 100.")
    # Include two different difficulty levels
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

    if difficulty == 'easy':
        easy_level(num, name)
    elif difficulty == 'hard':
        hard_level(num, name)


play_game()
  