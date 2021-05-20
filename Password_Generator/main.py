#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


password = ""
rand_letters = ""
for i in range(nr_letters):
  result = random.choice(letters)
  rand_letters = rand_letters + result
#print(rand_letters)

rand_symbols = ""
for i in range(nr_symbols):
  result = random.choice(symbols)
  rand_symbols = rand_symbols + result
#print(rand_symbols)

rand_numbers = ""
for i in range(nr_numbers):
  result = random.choice(numbers)
  rand_numbers = rand_numbers + result
#print(rand_numbers)

temp_pass = rand_letters + rand_numbers + rand_symbols
#print(temp_pass)

# temp_list = list(temp_pass)
# random.shuffle(temp_list)
# password = password.join(temp_list)

password = password.join(random.sample(temp_pass, len(temp_pass)))

print(f"Your password is: {password}")