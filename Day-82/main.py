from data import key_values

input_str = input("Enter a string: ")
output = ""

for letter in input_str:
    output += key_values[letter.upper()]

print(f"The string in morse code is: {output}")

