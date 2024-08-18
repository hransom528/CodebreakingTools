# Harris Ransom
# Affine Cipher Solver
# 8/4/2024

# Imports
import argparse
import re
from sys import path
path.append('../frequencyAnalysis')
import ngramScore
from pycipher import Affine

# Define key alphabet
a = [1,3,5,7,9,11,15,17,19,21,23,25]
b = list(range(26))

# Break Affine cipher
# See: http://www.practicalcryptography.com/cryptanalysis/stochastic-searching/cryptanalysis-affine-cipher/
def breakAffine(ciphertext):
    # Initialize ngram score
    ns = ngramScore.ngram_score('../frequencyAnalysis/data/english_quadgrams.txt')

    # Try all possible keys, return the best one
    scores = []
    for i in a:
        scores.extend([(ns.score(Affine(i,j).decipher(ciphertext)),(i,j)) for j in range(0,25)])
    return max(scores)

# MAIN
if __name__ == "__main__":
    # Parse user input

    #parser = argparse.ArgumentParser(description="Affine Cipher Solver")
    # Add your command line arguments here
    #args = parser.parse_args()
    ciphertext = input("Enter the Affine ciphertext: ")
    ciphertext = re.sub('[^A-Z]','',ciphertext.upper())

    # Break the Affine cipher
    bestKey = breakAffine(ciphertext)
    print('best candidate with key (a,b) = '+str(bestKey[1])+':')
    print(Affine(bestKey[1][0], bestKey[1][1]).decipher(ciphertext))

# Test ciphertext: QUVNLAUVILZKVZZZVNHIVQUFSFZHWZQLQHQLJSNLAUVI