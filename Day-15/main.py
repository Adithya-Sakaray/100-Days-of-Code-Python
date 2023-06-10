from data import resources,MENU 
from os import system

system("cls")

money = 0

def printReport():
    print("Report:")
    print(f"Water: {resources['water']}")
    print(f"Milk: {resources['milk']}")
    print(f"Coffee: {resources['coffee']}")
    print(f"Money: ${money}")

def takeMoney(choice):
    global money
    """Handles the money"""

    requiredMoney = MENU[choice]["cost"]
    print(f"Cost of {choice}: {requiredMoney}") 
    print("Insert coins:")
    
    pennies = int(input("Pennies:"))
    nickels = int(input("Nickels:"))
    dimes = int(input("Dimes:"))
    quarters = int(input("Quarters:"))

    totalMoney = (pennies*0.01) + (nickels*0.05) + (dimes*0.10) + (quarters*0.25)

    
    if totalMoney > requiredMoney :
        money += requiredMoney
        change = round(totalMoney - requiredMoney,2)
        print(f"Keep the change: ${change}")
        return True
    elif totalMoney == requiredMoney :
        money += requiredMoney
        print("Thank you for providing exact change")
        return True
    else:
        print("Not enough money!!The money is refunded")
        return False
    

def makeCoffee(choice):

    waterReq = MENU[choice]["ingredients"]["water"]
    milkReq = MENU[choice]["ingredients"]["milk"]
    coffeeReq = MENU[choice]["ingredients"]["coffee"]

    resources["water"] -= waterReq
    resources["milk"] -= milkReq
    resources["coffee"] -= coffeeReq

    print(f"Here is your {choice} ☕ Enjoy!!")

def resourcesAvailabe(choice):
    waterReq = MENU[choice]["ingredients"]["water"]
    milkReq = MENU[choice]["ingredients"]["milk"]
    coffeeReq = MENU[choice]["ingredients"]["coffee"]

    waterAvail = resources["water"]
    milkAvail = resources["milk"]
    coffeeAvail = resources["coffee"]

    if (waterAvail<waterReq or coffeeAvail<coffeeReq or milkAvail<milkReq):
        return False
    else:
        return True

        
    


def main():
    choice = input("What do you want (espresso/latte/cappuccino):")

    if choice == "report":
        printReport()
        main()

    elif choice == "espresso" or choice == "latte" or choice == "cappuccino":
        if(resourcesAvailabe(choice)):
            if(takeMoney(choice)):
                makeCoffee(choice)
        else:
            print("Not enought ingredients left!!")
            print("Please visit next time!")
        main()

    elif choice == "off":
        print("Thank you for using the machine!!")
        return
    else:
        print("Please enter a valid input")
        main()

main()
