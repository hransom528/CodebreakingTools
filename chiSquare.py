# Harris Ransom
# Frequency Analysis - Chi-Square Test
# 8/3/2024

# Imports
from freqAnalysis import englishFrequencies

# Calculate Chi-Squared statistic for a given text
def chiSquare(text):
    n = len(text)
    chiSquareStat = 0

    for char in englishFrequencies.keys():
        observed = text.count(char)
        expected = n * englishFrequencies[char]
        if (not expected):
            continue
        chiSquareStat += (((observed - expected) ** 2) / expected)

    return chiSquareStat

# Main
if __name__ == "__main__":
    # Get user input
    print("Enter the text you want to analyze: ")
    text = input().lower().strip()

    # Perform the chi-square test
    chiSquareStat = chiSquare(text)
    print(f"Chi-Squared Statistic: {chiSquareStat}")

# Test Inputs:
# WHENTHECLOCKSTRIKESTWELVEATTACK, X2 = 51.92133
# THWKEEVIWTETSCANHKERCTTAKSCLLOE, X2 = 51.92133
# ZDXPLXTDOWXSWCRSGPWVVOCWEOTTXOK, X2 = 425.59631