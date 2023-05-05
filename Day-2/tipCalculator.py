totalAmount = float(input("What was the total bill? $"))
tipPercent = int(input("What percentage tip would you like to give? 10,12 or 15?"))
people = int(input("How many people are spliting the bill? "))

totalWithTip = totalAmount + (totalAmount*(tipPercent/100))
splitAmongPeople = totalWithTip/people
splitFormatted = "{:.2f}".format(round(splitAmongPeople))

print(f"Each person should pay {splitFormatted}")