from art import logo
import random
import os


def checkNumber(guessedNumber,realNumber):
    global attempts
    global gameWon
    if(guessedNumber == realNumber):
        print("You got It!!!")
        print("Voila")
        print(f"The answer is {realNumber}")
        gameWon = True
        attempts = -1
    elif(guessedNumber > realNumber):
        print("Too High")
        attempts -= 1
    else:
        print("Too Low")
        attempts -= 1



realNumber = random.randint(1,100)
gameWon = False

os.system("cls")
print(logo)
print("Welcome to the number guessing game!!")
print("Guess a number between 1 and 100.")
print("Corerct answer:",realNumber)
difficulty = input("Choose a difficulty. Type 'easy' or 'hard':")




#setting the number of attempts accorging to difficulty
attempts = 10
if difficulty == "hard":
    attempts = 5

if difficulty== "hard" or difficulty == "easy":
    while(attempts>0):
        print(f"You have {attempts} attempts remaining to guess the number")
        guessedNumber = int(input("Guess the number:"))
        checkNumber(guessedNumber,realNumber)
        if attempts!= 0:
            print("Guess again") 
    if not gameWon:
        print("You have exhausted your attempts")
        print("You lose.Better luck next time!!")
else:
    print("Please enter a valid input")
    print("Restart the game to play again!!")
