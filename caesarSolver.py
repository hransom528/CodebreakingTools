# Harris Ransom
# Caesar Cipher Solver
# 6/18/2024

# Imports
import string
from sys import path

path.append('frequencyAnalysis')
from chiSquare import chiSquare

# Defines character alphabet
alphabet = string.ascii_lowercase

# Shifts a string by a given offset
def shift_string(inputStr, offset):
    str = list(inputStr)
    for i in range(0, len(str)):
        if str[i] in alphabet:
            charNum = alphabet.index(str[i])
            charNum = (charNum + offset) % 26
            str[i] = alphabet[charNum]
    return "".join(str)

# Caesar Cipher Solver
def caesarSolver(text):
    print("Key \t Decoded Text ".ljust(len(text) + 13) + "Chi-Squared")
    for base in range (0, 26):
        shiftedString = shift_string(text, base)
        print(f"{base} \t {shiftedString} \t {chiSquare(shiftedString)}")

# MAIN
def main():
    # Get user input
    print("Enter the ciphertext: ")
    text = input().lower().strip()
    caesarSolver(text)

# Dunder main
if __name__ == "__main__":
    main()

# Test text: Devhqfh vkdushqv oryh, suhvhqfh vwuhqjwkhqv lw. Ehqmdplq Iudqnolq
# Test text 2: snszk kxchr zakdc knmfh stcde nqsxk zshst cdrdu dmsxs gqdd