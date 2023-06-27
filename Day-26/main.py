import pandas

# creating a dictionary form csv
data_df = pandas.read_csv("nato_phonetic_alphabet.csv")
data = {rows["letter"]: rows["code"] for (index, rows) in data_df.iterrows()}

# getting user input and printing the list
user_input = input("Enter a word (only alphabets): ").upper()
result = [data[x] for x in user_input]
print(result)



