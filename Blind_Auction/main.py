import os

from art import logo
print(logo)

clear = lambda: os.system('cls')

auction = {}
bidding_finish = False

def highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""
  for bidder in bidding_record:
    bid_amount = int(bidding_record[bidder])
    if bid_amount > highest_bid :
      highest_bid = bid_amount
      winner = bidder
      
  print(f"The winner is {winner} with a bid of ₹{highest_bid}")

while not bidding_finish:
  name = input("What is your Name?: ")
  bid = input("What is your bid?: ₹")
  auction[name] = bid
  bider = input("Are there any other bidders? Type 'yes or 'no'.\n").lower()
  if(bider == "yes"):
    clear()
  elif(bider == "no"):
    bidding_finish = True
    highest_bidder(auction)
  else:
    print("Please enter Yes or No.")