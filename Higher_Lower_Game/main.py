import random
import os
from art import logo, vs
from game_data import data

clear = lambda: os.system('cls')

def get_random_data():
    """Get random data from game_data list"""
    compare = random.choice(data)
    return compare
  
def compare_answer(a_followers, b_followers, guess):
    """Checks followers against user's guess 
    and returns True if they got it right.
    Or False if they got it wrong.""" 
    if a_followers > b_followers:
        return guess == 'a'
    elif b_followers > a_followers:
        return guess == 'b'

def game():
  score = 0
  compare1 = get_random_data()
  compare2 = get_random_data()
  is_game_over = False
  while not is_game_over:
      # Make B become the next A.
        compare1 = compare2
        compare2 = get_random_data()

        if compare1 == compare2:
            compare2 = get_random_data()

        # Print logo
        print(logo)
        print(f"Compare A: {compare1['name']}, a {compare1['description']}, from {compare1['country']}.")
        print(compare1['follower_count'])
        print(vs)

        print(f"Against B: {compare2['name']}, a {compare2['description']}, from {compare2['country']}.")
        print(compare2['follower_count'])
        a_followers = compare1['follower_count']
        b_followers = compare2['follower_count']
        # Ask user for a guess.
        user_ans = input("Who has more followers? Type 'A' or 'B': ").lower()
        is_correct = compare_answer(a_followers, b_followers, user_ans)

        # Clear screen between rounds.
        clear()
        print(logo)

        # Score Keeping.
        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}.")
        else:
            is_game_over = True
            print(f"Sorry, that's wrong. Final score: {score}")

game()