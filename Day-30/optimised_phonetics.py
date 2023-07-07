import pandas

# creating a dictionary form csv
data_df = pandas.read_csv("nato_phonetic_alphabet.csv")
data = {rows["letter"]: rows["code"] for (index, rows) in data_df.iterrows()}


def generate_phonetic():
    user_input = input("Enter a word: ").upper()
    try:
        result = [data[x] for x in user_input]
    except KeyError:
        print("Please enter only alphabets!")
        generate_phonetic()
    else:
        print(result)


generate_phonetic()
