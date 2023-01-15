import os
#HINT: You can call clear() to clear the output in the console.
from art import logo

print(logo)
print("Welcome to the Secret Auction Program\n")

bidding_data = {}
end = False

def find_winner(bidding_data):
  highest_bid = 0
  winner = ''
  for bidder in bidding_data:
    new_bid = bidding_data[bidder]
    if new_bid > highest_bid:
      highest_bid = new_bid
      winner = bidder
  print()
  #print(winner)
  #print(highest_bid)
  print(f"{winner} is the winner with highest bid of $ {highest_bid} \n")
  
while not end:
  name = input("What is your name?: ")
  bid = int(input("What's your bid?: $ "))
  bidding_data[name] = bid
  bidders = input("Are their any other bidders? Type yes or no: ").lower()
  if bidders == "no":
    end = True
    find_winner(bidding_data)
  elif bidders == "yes":
      os.system('clear')


  
