from money_machine import MoneyMachine
from menu import Menu,MenuItem
from coffee_maker import CoffeeMaker
from os import system

system("cls")
shouldContinue = True

moneyMachineObj = MoneyMachine()
menuObj = Menu()
coffeeMakerObj = CoffeeMaker()

while(shouldContinue):
    choice = input("What would you like? (espresso/latte/cappuccino):")

    if(choice == "off"):
        shouldContinue = False
    elif (choice == "report"):
        coffeeMakerObj.report()
        moneyMachineObj.report()
    elif (choice == "espresso" or choice == "latte" or choice == "cappuccino"):
        item = menuObj.find_drink(choice)
        if(item is not None):
            if (coffeeMakerObj.is_resource_sufficient(item)):
                if (moneyMachineObj.make_payment(item.cost)):
                    coffeeMakerObj.make_coffee(item)
    else:
        print("Invalid input, Please try again")

