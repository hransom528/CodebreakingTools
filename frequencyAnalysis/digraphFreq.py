# Harris Ransom
# Digraph Counter
# 6/19/2024

# Imports
import string
import matplotlib.pyplot as plt

# Defines character alphabet
alphabet = string.ascii_uppercase

# Plot digraph frequency analysis
def plotDigraphFreq(freqDict):
    fig, ax = plt.subplots(figsize=(20, 3))
    fig.tight_layout()
    rects = ax.bar(freqDict.keys(), freqDict.values(), align='center', width=0.5)
    ax.bar_label(rects, freqDict.values())
    ax.set_xlabel("Digraphs")
    ax.set_ylabel("Frequency")
    ax.set_title("Digraph Frequency Analysis")
    plt.show()

# Count the frequency of each digraph in the text
def digraphFreq(str):
    freqDict = {}
    total = 0

    # Remove non-alphabetic characters
    for char in str:
        if char not in alphabet:
            str = str.replace(char, "")

    # Count digraphs
    for i in range(len(str) - 1):
        digraph = str[i] + str[i + 1]
        if str[i] not in alphabet or str[i + 1] not in alphabet:
            continue
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

    return freqDict

# Main
def main():
    # Get user input
    print("Enter the text you want to analyze: ")
    text = input().upper().strip()

    # Count the frequency of each digraph in the text
    freqDict = digraphFreq(text)

    # Plot digraph frequency analysis
    plotDigraphFreq(freqDict)

# Dunder main
if __name__ == "__main__":
    main()

# Test text (NSA Monday Challenge #1):
# tpfccdlfdtte pcaccplircdt dklpcfrp?qeiq lhpqlipqeodf gpwafopwprti izxndkiqpkii krirrifcapnc dxkdciqcafmd vkfpcadf