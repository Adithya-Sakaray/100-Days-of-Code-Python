import art
def caesar(direction):
    
    if direction == "encode":
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        if shift>25:
            shift = shift % 26
        encryptedText=""
        for i in text:
            tempIndex = alphabet.index(i)
            newIndex = tempIndex+shift
            if(newIndex>25):
                newIndex = newIndex - 25 -1
            encryptedText += alphabet[newIndex]
        
        print(f"Encrypted text is: {encryptedText}")
    elif direction == "decode":
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        if shift>25:
            shift = shift % 26
        decryptedText=""
        for i in text:
            tempIndex = alphabet.index(i)
            newIndex = tempIndex-shift
            if(newIndex<0):
                newIndex = 25 + newIndex +1
            decryptedText += alphabet[newIndex]
        
        print(f"The Decrypted text is: {decryptedText}")
    else:
        print("Please enter valid command")
        


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
choice = "yes"

print(art.logo)

while (choice == "yes"):
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    
    caesar(direction=direction)

    choice=input("Enter \"yes\" to continue, else enter \"no\" to exit:")

if choice == "no":
    print("Exitted sucessfully!!!")
else:
    print("Invalid command entered, program is exitted...")

