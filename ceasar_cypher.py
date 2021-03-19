''' creating a function where user messages are encoded by their choice of shift amount. When receiving an encoded message, it can be decrypted by the same shift amount.
'''
''' 
# 1: create a list with the alphabet
# 2: create variables for direction : encode or decode
# 3: create variable for text
# 4: create a variable for shift
# 5: define a function that will allow the user to input text that can be encoded or decoded by their shift amount in the list of alphabet letters

'''



alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# While loop to allow user to choose to continue or not. if not, exit the program by setting boolean to False
should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift = shift % 26

    result = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if result == 'no':
        should_continue = False
        print("Goodbye")

# using 3 parameters. those parameters include the variables for choices of text, shift amount, and either decode or encode
'''looping through each character in inputed text, and if it is in alphabet, replacing that character with the index of the alphabet list. Then, taking that index, adding the shift amount and then adding that new index to end_text'''
def caesar(start_text, shift_amount, cipher_direction):
    # creating a empty string for endcoded or decoded message
    end_text = ""
    if cipher_direction == "decode":
            # subtracting shift amount by user shift input
            shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position] 
        else: 
            end_text += char
    print(f"The {cipher_direction}d text is {end_text}")


caesar(start_text = text, shift_amount = shift, cipher_direction = direction)

        




