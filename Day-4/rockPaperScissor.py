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

#Write your code below this line 👇
choiceList = [rock,paper,scissors]
userSelection = int(input("What do you choose? Type 0 for rock,1 for paper, 2 for scissors\n"))

print(f"You chose:\n{choiceList[userSelection]}")

computerSelection = random.randint(0,2)

print(f"The computer chose:\n{choiceList[computerSelection]}")

if(computerSelection == userSelection):
  print("The match is drawn")
elif(computerSelection==0):
  if(userSelection==1):
    print("You win!!")
  else:
    print("You lose!!")
elif(computerSelection == 1):
  if(userSelection==0):
    print("You lose!!")
  else:
    print("You win!!")
elif(computerSelection == 2):
  if(userSelection==0):
    print("You win!!")
  else:
    print("You lose!!")
  