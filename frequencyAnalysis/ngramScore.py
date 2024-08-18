# Harris Ransom
# Score text using n-gram probabilities
# 8/3/2024
# See: http://www.practicalcryptography.com/media/cryptanalysis/files/ngram_score_1.py

# Imports
from math import log10

# ngram_score class
class ngram_score(object):

    # Load a file containing ngrams and counts, calculate log probabilities
    def __init__(self,ngramfile,sep=' '):
        # Load file with error handling
        with open(ngramfile, 'r') as f:
            self.ngrams = {}
            lineCount = 0
            lines = f.readlines()
            for line in lines:
                key,count = line.split(sep) 
                self.ngrams[key] = int(count)
                lineCount += 1

        self.lineCount = lineCount
        self.L = len(key)
        self.N = sum(self.ngrams.values())

        # Calculate log probabilities
        for key in self.ngrams.keys():
            self.ngrams[key] = log10(float(self.ngrams[key])/self.N)
            #print(f"{self.ngrams[key]}")
        self.floor = log10(0.01/self.N)

        # Calculate normal fitness
        self.nfitness = self.calcNormalFitness()

    # Get ngram probabilities
    def getNgramProbs(self):
        return self.ngrams

    # Get the normal fitness of English ngrams
    def getNormalFitness(self):
        return self.nfitness

    # Calculate and store the fitness of normal English ngrams
    def calcNormalFitness(self):
        fitness = sum(self.ngrams.values())
        fitness /= self.lineCount
        return fitness

    # Compute score of text
    def score(self,text):
        text = text.replace(" ", "")
        score = 0.0
        #ngrams = self.ngrams.__getitem__
        for i in range(len(text)-self.L+1):
            ngram = text[i:i+self.L]
            if ngram in self.ngrams:
                prob = self.ngrams[ngram]
            else: 
                prob = self.floor   
            score += prob
            #print(f"ngram: {ngram} \t p: {prob} \t score: {score}")
        return score