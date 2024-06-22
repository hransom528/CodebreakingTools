# Harris Ransom
# Triple Letter Digraph Counter
# 6/21/2024

# Imports
import string
import matplotlib.pyplot as plt

# Defines character alphabet
alphabet = string.ascii_uppercase

# Count the frequency of each digraph in the text
def digraphFreq(str):
    freqDict = {}
    total = 0

    # Remove non-alphabetic characters
    for char in str:
        if char not in alphabet:
            str = str.replace(char, "")

    # Count digraphs
    for i in range(len(str) - 2):
        digraph = str[i] + str[i + 1] + str[i + 2]
        if digraph in freqDict:
            freqDict[digraph] += 1
        else:
            freqDict[digraph] = 1
        total += 1
    
    # Sort freqDict
    freqDict = dict(sorted(freqDict.items(), key=lambda item: item[1], reverse=True))

    # Print the frequency of each digraph
    for digraph in freqDict:
        print(f"{digraph}: {freqDict[digraph]}")

    # Plot digraph frequency analysis
    fig, ax = plt.subplots(figsize=(20, 3))
    fig.tight_layout()
    rects = ax.bar(freqDict.keys(), freqDict.values(), align='center', width=0.5)
    ax.bar_label(rects, freqDict.values())
    ax.set_xlabel("Triple Digraphs")
    ax.set_ylabel("Frequency")
    ax.set_title("Triple Letter Digraph Frequency Analysis")
    plt.show()
    
# Main
def main():
    # Get user input
    print("Enter the text you want to analyze: ")
    text = input().upper().strip()
    digraphFreq(text)

# Dunder main
if __name__ == "__main__":
    main()

# Test text (NSA Monday Challenge #1):
# tpfccdlfdtte pcaccplircdt dklpcfrp?qeiq lhpqlipqeodf gpwafopwprti izxndkiqpkii krirrifcapnc dxkdciqcafmd vkfpcadf