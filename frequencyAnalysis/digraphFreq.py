# Harris Ransom
# Digraph Counter
# 6/19/2024

# Imports
import string

# Defines character alphabet
alphabet = string.ascii_lowercase

# Count the frequency of each digraph in the text
def digraphFreq(str):
    freqDict = {}
    total = 0
    

# Main
def main():
    # Get user input
    print("Enter the text you want to analyze: ")
    text = input().lower()
    digraphFreq(text)

# Dunder main
if __name__ == "__main__":
    main()