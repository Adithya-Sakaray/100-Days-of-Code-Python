import os
from art import logo

def add (n1,n2):
  return round(n1+n2,2)

def subtract(n1,n2):
  return round(n1-n2,2)

def multiply(n1,n2):
  return round(n1*n2,2)

def divide(n1,n2):
  return round(n1/n2,2)

operations = {
  "+":add,
  "-":subtract,
  "*":multiply,
  "/":divide,
}

def calculator():
  os.system("cls")
  print(logo)
  num1 = float(input("Enter first number:"))
  for key in operations:
    print(key)
  
  shouldContinue = True
  while (shouldContinue):
    operation_symbol = input("Pick an operation:")
    num2 = float(input("Enter The other number:"))
    answer = operations[operation_symbol](num1,num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    
    choice = input(f"Type 'y' to continue calculating with {answer},type 'n' to start new or type 'e' to exit:").lower()
    if (choice == "y"):
      num1 = answer
    elif (choice == "n"):
      shouldContinue = False
      calculator()
    elif (choice == "e"):
      print("Successfully exited...")
      shouldContinue = False  
    else:
      print("Invalid command entered, exiting...")
      shouldContinue = False

calculator()