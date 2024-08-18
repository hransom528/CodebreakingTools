# Harris Ransom
# Simple Substitution Cipher - Solver Tool
# 6/18/2024

# Imports
import string

# Defines character alphabet
englishChars = string.ascii_lowercase
alphabet = dict.fromkeys(englishChars)

'''
alphabet = {
    'a': ,
    'b': ,
    'c': ,
    'd': ,
    'e': ,
    'f': ,
    'g': ,
    'h': ,
    'i': ,
    'j': ,
    'k': ,
    'l': ,
    'm': ,
    'n': ,
    'o': ,
    'p': ,
    'q': ,
    'r': ,
    's': ,
    't': ,
    'u': ,
    'v': ,
    'w': ,
    'x': ,
    'y': ,
    'z': 
}'''

# Substitute in defined alphabet
def substitute(text, alphabet):
    # Substitute each letter in the text
    for char in text:
        if char in alphabet.keys():
            text = text.replace(char, alphabet[char])

    print(text)
    return text


# Main
def main():
    # Get user input
    print("Enter the simple substitution ciphertext you want to analyze: ")
    text = input().lower()
    substitute(text)

# Dunder main
if __name__ == "__main__":
    main()