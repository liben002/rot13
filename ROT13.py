# This program encrypts and decrypts using ROT13
inputUpper = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
inputLower = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

message = input('Please enter message to encrypt/decrypt: ')
message = list(message)
newMessage = ''

# goes throught each character in the message and if it's alpha, encode/decode. Otherwise just concatenate.
for character in message:
    if character.isalpha():
        if character.islower():
            if inputLower.index(character) < 13:
                newMessage += inputLower[inputLower.index(character) + 13]
            else:
                newMessage += inputLower[13 - (25 - inputLower.index(character))]
        else:
            if inputUpper.index(character) < 13:
                newMessage += inputUpper[inputUpper.index(character) + 13]
            else:
                newMessage += inputUpper[13 - (25 - inputUpper.index(character))]
    else:
        newMessage += character
print('The encrypted/decrypted message is: ' + newMessage)
