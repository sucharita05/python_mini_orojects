import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

image = [rock, paper, scissors]
user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: \n"))

if (user_input >= 3 or user_input < 0):
  print("You typed an invalid number, You Lose!")

print(f"You Choose: \n {image[user_input]}")


computer_input = random.randint(0, 2)
print(f"Computer Choose: \n {image[computer_input]}")

if (user_input == 0 and computer_input == 2):
  print("You Won!")
elif (user_input == 2 and computer_input == 1):
   print("You Won!")
elif (user_input == 1 and computer_input == 0):
   print("You Won!")
elif (user_input == computer_input):
   print("It's a draw!")
else:
  print("You Lose!")
