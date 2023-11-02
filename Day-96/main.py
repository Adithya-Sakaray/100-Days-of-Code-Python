import requests


def get_definition(word):
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    response = requests.get(url=url)

    if response.status_code == 200:
        try:
            response = response.json()
            meanings = response[0]["meanings"][0]
            define = meanings["definitions"][0]["definition"]
            part_ofspeech = meanings["partOfSpeech"]
        except:
            return "", ""

        return part_ofspeech, define


input_word = input("Enter a word: ")
part_of_speech, definition = get_definition(input_word)

if len(part_of_speech) == 0 and len(definition) == 0:
    print("Enter a valid word")
else:
    print(f"{input_word} is a {part_of_speech}")
    print(f"It's definition is: {definition}")
