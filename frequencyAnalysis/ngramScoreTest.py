# Harris Ransom
# ngramScore Testing
# 8/18/2024

# Imports
import ngramScore

# Test ngramScore class
def testNgramScore():
    # Define test data
    testText1 = "ATTACK THE EAST WALL OF THE CASTLE AT DAWN"
    testText2 = "FYYFHP YMJ JFXY BFQQ TK YMJ HFXYQJ FY IFBS"

    # Initialize ngram_score class
    print("Testing ngram_score class...")
    ns = ngramScore.ngram_score("data/english_quadgrams.txt")
    ngrams = ns.getNgramProbs()
    normFitness = ns.getNormalFitness()

    # Calculate fitness of test data
    score1 = ns.score(testText1)
    score2 = ns.score(testText2)

    # Print results
    #print(f"ngrams: {ngrams}")
    print(f"Normal Fitness: {normFitness}")
    print(f"Score of text1: {score1} \t Expected: -129.24")
    print(f"Score of text2: {score2} \t Expected: -288.10")

# MAIN
if __name__ == "__main__":
    testNgramScore()