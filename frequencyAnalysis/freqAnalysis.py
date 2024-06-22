# Harris Ransom
# Cryptographic Frequency Analysis
# 6/17/2024

# Imports
import string
import matplotlib.pyplot as plt
#matplotlib.use('Agg')

# Defines character alphabet
alphabet = string.ascii_lowercase

# Defines English alphabet frequencies
englishFrequencies = {
    'a': 0.08167,
    'b': 0.01492,
    'c': 0.02782,
    'd': 0.04253,
    'e': 0.12702,
    'f': 0.02228,
    'g': 0.02015,
    'h': 0.06094,
    'i': 0.06966,
    'j': 0.00153,
    'k': 0.00772,
    'l': 0.04025,
    'm': 0.02406,
    'n': 0.06749,
    'o': 0.07507,
    'p': 0.01929,
    'q': 0.00095,
    'r': 0.05987,
    's': 0.06327,
    't': 0.09056,
    'u': 0.02758,
    'v': 0.00978,
    'w': 0.02360,
    'x': 0.00150,
    'y': 0.01974,
    'z': 0.00074
}
englishFrequencies = dict(sorted(englishFrequencies.items(), key=lambda item: item[1], reverse=True))


# Frequency Analysis
def freqAnalysis(text):
    # Create dictionary to store letter frequencies
    freqDict = {}
    total = 0
    for letter in alphabet:
        freqDict[letter] = 0

    # Count the frequency of each letter in the text
    for letter in text:
        if letter in alphabet:
            freqDict[letter] += 1
            total += 1

    # Sort freqDict
    freqDict = dict(sorted(freqDict.items(), key=lambda item: item[1], reverse=True))

    # Print the frequency of each letter
    for letter in freqDict:
        print(f"{letter}: {freqDict[letter]}")

    # Gets relative frequency of each letter
    print("\nRelative Frequencies:")
    frequencies = []
    for letter in freqDict:
        letterFrequency = (freqDict[letter] / float(total)) #* 100
        frequencies.append(letterFrequency)
        print(f"{letter}: {letterFrequency:.4f}")

    # Plot the relative frequencies
    fig, (ax1, ax2) = plt.subplots(2)

    rects = ax1.bar(range(len(freqDict)), frequencies, align='center')
    ax1.set_xticks(range(len(freqDict)), list(freqDict.keys()))
    ax1.set_title("Text Letter Frequencies")
    ax1.bar_label(rects, [format(frequency, '.2f') for frequency in frequencies])

    rects2 = ax2.bar(range(len(englishFrequencies)), list(englishFrequencies.values()), align='center')
    ax2.set_xticks(range(len(englishFrequencies)), list(englishFrequencies.keys()))
    ax2.set_title("English Letter Frequencies")
    ax2.bar_label(rects2, [format(frequency, '.2f') for frequency in list(englishFrequencies.values())])
    plt.show()

# Main
def main():
    # Get user input
    print("Enter the text you want to analyze: ")
    text = input().lower().strip()
    freqAnalysis(text)

# Dunder main
if __name__ == "__main__":
    main()

# Test text: 
#CENERENTOLA.- N bnxm yt ywd nk dtz hfs wjfi ymnx fsi fr rtxy fscntzx yt mjfw ymfy fsi, bmjs dtz wjyzws, fsi mtb qtsl dtzwjrfns, mjwj. It bwnyj f kjb qnsjx ifwqnsl, uqjfxj. N mfaj gjjs ajwd kfw kwtr mfuud xnshj dtz bjsy fbfd.

# Test text 2 (NSA Monday Challenge #1):
# tpfccdlfdtte pcaccplircdt dklpcfrp?qeiq lhpqlipqeodf gpwafopwprti izxndkiqpkii krirrifcapnc dxkdciqcafmd vkfpcadf
