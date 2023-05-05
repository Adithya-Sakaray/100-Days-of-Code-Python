import art
import os

data_dict = {}

choice = "yes"
max_price = 0
max_name = ""

print(art.logo)
print("Welcome to secret aution game!!")
while (choice == "yes"):
  name = input("What is your name?: ")
  bid = int(input("What's your bid?: "))
  
  data_dict[name] = bid
  max_price = bid
  
  
  choice = input("Are the any other bidders?type \"yes\" or \"no\": ").lower()
  os.system("cls")
  
 

for name in data_dict:
  price = data_dict[name]
  if(price > max_price):
    max_price = price
    max_name = name

if (choice != "no"):
   print("Invalid command entered exitting the game...")


print(f"The winner with maximum bid is {max_name} with a bid of ${max_price}")
print(f"Congratulations on the victory!!!!!")


