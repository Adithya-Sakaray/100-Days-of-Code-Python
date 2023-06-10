import art
import os
from data import data
import random

random.shuffle(data)

score = 0
currentDataIndex = 0
isFirst = True
isGoing = True


def getRandomData():
    return random.choice(data)



def game():
    global score
    global currentDataIndex
    global isFirst
    global isGoing

    os.system("cls")
    print(art.logo)
    if(not isFirst):
        print(f"You guessed right!! Your score is: {score}")
    currentData = getRandomData()
    nextData = getRandomData()
    while(isGoing):
        currentData = nextData
        nextData = getRandomData()
        while currentData == nextData:
            nextData = getRandomData()
        isFirst = False
        print(f"Compare A: {currentData['name']}, {currentData['description']}, from {currentData['country']}")
        print(art.vs)
        print(f"Against B:{nextData['name']}, {nextData['description']}, from {nextData['country']}")
        enteredValue = input("Who has more followers? type 'A' or 'B':")

        if(enteredValue == "B" and nextData['follower_count']>currentData['follower_count']):
            score += 1
            os.system("cls")
            print(art.logo)
            print(f"You guesses right!! Current score:{score}")

        elif (enteredValue == "A" and nextData['follower_count']<currentData['follower_count']):
            score += 1
            os.system("cls")
            print(art.logo)
            print(f"You guesses right!! Current score:{score}")
        else:
            os.system("cls")
            print(art.logo)
            print(f"You lose!! Final score:{score}")
            isGoing = False
            break



game()

