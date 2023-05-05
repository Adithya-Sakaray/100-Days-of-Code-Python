import random
import hangman_art as art
import hangman_words as words


chosen_word = random.choice(words.word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6


print(art.logo)
print()

#Testing code
#print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
selected = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    print()


    if guess in display:
        print(f"You have already entered '{guess}', please select other letter")
        
    

    

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        if guess in selected:
            print(f"You have already entered '{guess}', please select other letter")
            print(f"You have {lives} lives remaining!!!")
            
        else:
            print(f"The letter '{guess}' is not in the word,you lose a life")
            lives -= 1
            print(f"You have {lives} lives remaining!!!")
            if lives == 0:
                end_of_game = True
                print("You lose.WASTED!!!")
                print(f"The correct word is:{chosen_word}")

    #Join all the elements in the list and turn it into a String.
    selected.append(guess)
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("YAAY!!!!!!!You win.")

    print(art.stages[lives])