# ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13
# letters after it in the alphabet. ROT13 is an example of the Caesar cipher.
# Create a function that takes a string and returns the string ciphered with Rot13. If
# there are numbers or special characters included in the string, they should be returned
# as they are. Only letters from the latin/english alphabet should be shifted, like in
# the original Rot13 "implementation".
# Please note that using encode is considered cheating.

def rot13(message):
    alphabet_l = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
        'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
        's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    ]

    alphabet_u = [
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
        'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
        'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
    ]

    message = list(message)
    encode_message = ''

    for letter in message:
        if letter not in alphabet_l and letter not in alphabet_u:
            encode_message += letter
        elif letter.upper() == letter:
            index = alphabet_u.index(letter) + 13
            encode_message += alphabet_u[index % 26]
        else:
            index = alphabet_l.index(letter) + 13
            encode_message += alphabet_l[index % 26]

    return encode_message


print(rot13("A"))
