import os
from art import logo

clear = lambda: os.system('cls')

# Calculator
# Add
def add(n1, n2):
  return n1 + n2

# Subtract
def subtract(n3, n4):
  return n3 - n4

# Multiply
def multiplay(n5, n6):
  return n5 * n6

# Divide
def divide(n7, n8):
  return n7 / n8

# Calculator Dictionry
operations = {"+": add, 
"-": subtract,
"*": multiplay,
"/": divide
}

def calculator():
  print(logo)
  num1 = float(input("What is the first number?: "))

  for operator in operations:
    print(operator)

  continue_calculate = True

  while continue_calculate:
    choosen_operator = input("Pick an operation: ")
    num2 = float(input("What is the next number?: "))

    calculation = operations[choosen_operator]
    answer = calculation(num1, num2)

    print(f"{num1} {choosen_operator} {num2} = {answer}")

    user_input = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation, or type 'e' to exit ").lower()
    if (user_input == 'y'):
      num1 = answer
    elif (user_input == 'n'):
      continue_calculate = False
      clear()
      calculator()
    elif (user_input == 'e'):
      continue_calculate = False
      clear()
    else:
      print("Please type 'y' or 'n'")


calculator()