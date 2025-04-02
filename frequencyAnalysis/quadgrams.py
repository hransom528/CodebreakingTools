# Harris Ransom
# Quadgram Frequency Analysis
# 8/18/2024
# See: http://www.practicalcryptography.com/cryptanalysis/text-characterisation/quadgrams/
# Motivation: Quadgrams are particularly helpful when performing frequency analysis on text (especially small text samples)

# Imports
from math import log10, log
import ngramScore

# Get quadgram frequencies
def getQuadgrams(text):
    # Clean text
    text = text.upper().strip()
    
    # Get text length
    n = len(text)
    if (n < 4):
        return
    
    # Count quadgrams
    quadCount = 0
    quadgrams = {}
    for i in range(n - 3):
        quadgram = text[i:i + 4]
        quadCount += 1
        if quadgram in quadgrams:
            quadgrams[quadgram] += 1
        else:
            quadgrams[quadgram] = 1

    # Normalize quadgram frequencies
    return quadgrams, quadCount

# Get normalized quadgram probabilities
# See: http://www.practicalcryptography.com/cryptanalysis/text-characterisation/quadgrams/
def getQuadgramProbs(quadgrams, quadCount):
    quadgramProbs = {}

    # Calculate normalized quadgram log probabilities
    for quadgram in quadgrams:
        quadgramProbs[quadgram] = log10(float(quadgrams[quadgram]) / quadCount)

    return quadgramProbs

# Calculate the fitness of the text based on quadgram probabilities
# See: https://planetcalc.com/8045/
def quadgramFitness(quadgramProbs, quadCount):
    # Calculate the fitness
    fitness = sum(quadgramProbs.values())
    fitness /= quadCount
    #print(f"Fitness: {fitness}")

    # Calculate difference between expected and actual frequencies
    ns = ngramScore.ngram_score("data/english_quadgrams.txt")
    normalFitness = ns.getNormalFitness()
    #print(f"Normal Fitness: {normalFitness}")
    fitness = float(abs(fitness - normalFitness) / normalFitness)
    return fitness

# MAIN
if __name__ == "__main__":
    # Get user input
    text = input("Enter the text you want to analyze: ")
    text = text.replace(" ", "")

    # Get quadgram frequencies
    quadgrams, quadCount = getQuadgrams(text)
    if (quadgrams == None):
        print("Text is too short to analyze.")
        exit()
    #print(f"Quadgram Count: {quadCount}")
    #print(f"Quadgrams: {quadgrams}")

    # Get quadgram probabilities
    quadgramProbs = getQuadgramProbs(quadgrams, quadCount)
    #print(sum(quadgramProbs.values()))

    # Calculate the fitness of the text
    fitness = quadgramFitness(quadgramProbs, quadCount)
    print(f"Fitness: {fitness}")