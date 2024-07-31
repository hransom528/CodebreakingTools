# Harris Ransom
# Index of Coincidence Calculator
# 6/18/2024

# Imports
import string

# Defines character alphabet
alphabet = string.ascii_lowercase

# Index of Coincidence
def IndexOfCoincidence(inputStr):
    # Initialize frequency dictionary
    freqDict = {}
    for letter in alphabet:
        freqDict[letter] = 0

    # Count the frequency of each letter in the text
    total = 0
    for char in inputStr:
        if char in alphabet:
            freqDict[char] += 1
            total += 1

    # Calculate the Index of Coincidence
    ioc = 0
    for letter in freqDict:
        freq = freqDict[letter]
        ioc += (float (freq * (freq - 1)) / float(total * (total - 1)))

    # Output the Index of Coincidence
    #print(f"Index of Coincidence: {ioc}")
    return ioc

# Main
def main():
    # Get user input
    print("Enter the text you want to analyze: ")
    text = input().lower()

    # Calculate the Index of Coincidence
    ioc = IndexOfCoincidence(text)
    print(f"Index of Coincidence: {ioc}")
    if (ioc > 0.06) and (ioc < 0.07):
        print("The text is likely English or a substitution cipher.")
    else:
        print("The text is likely not English, or is ciphered.")

# Dunder main
if __name__ == "__main__":
    main()

# Test text: ABC DCEFG FHI JBK LHM KGFKN OMPPHOK LHM JBK OGQLCDE GH DCEFG C FJRK SKKD GBLCDE GH ANHMBCOF J NCGGNK. FJRK SKKD HMG SBKJTCDE BHJQO GFCO JAGKBDHHD AHB GFK IJEHDO. EHHQ DCEFG