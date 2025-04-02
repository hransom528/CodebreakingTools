# Harris Ransom
# Hill Climber - Simple Substitution Cipher
# 6/23/2024

# Imports
import string
import random
from sys import path
path.insert(0, '../frequencyAnalysis')
path.append('../')
import freqAnalysis
import ngramScore
import indexOfCoincidence
#from chiSquare import chiSquare

# Defines character alphabet
alphabet = string.ascii_lowercase

# Generate random substitution table
def genSubTable():
	# Initialize subTable
	subTable = {}
	for char in alphabet:
		subTable[char] = ''

	# Generate a random mapping
	selectedLetterIndices = []
	selectedValues = []
	loopFlag = True
	while (loopFlag):
		randInd = random.randint(0, 25)
		# Check if the index has already been selected
		if randInd not in selectedLetterIndices:
			selectedLetterIndices.append(randInd)
			randChar = alphabet[randInd]
			
			# Generate a random unique substitution value
			randSubVal = random.randint(0, 25)
			while (randSubVal in selectedValues):
				randSubVal = random.randint(0, 25)
			selectedValues.append(randSubVal)

			subTable[randChar] = alphabet[randSubVal]

		# Check if all letters have been selected
		if len(selectedLetterIndices) == 26:
			loopFlag = False

	# Print the substitution table
	#for char in subTable:
	#	print(f"{char}: {subTable[char]}")

	return subTable

# Performs substitution on provided text using a substitution table
def substituteText(text, subTable):
	# Substitute the text
	subText = ""
	for char in text:
		if char in alphabet:
			subText += subTable[char]
		else:
			subText += char

	return subText

# Calculate the distance between the frequency of the text and the expected frequency
def calcFreqDistance(freqDict, expectedFrequencies):
	# Calculate the distance
	distance = 0
	for letter in freqDict:
		diff = abs(freqDict[letter] - expectedFrequencies[letter])
		distance += diff
		#print(f"Total Distance: {distance} \t Difference: {diff} \t Caculated Frequency: {freqDict[letter]} \t Expected Frequency: {expectedFrequencies[letter]}")
	return distance

# Perform a random swap on the substitution table
def permute(subTable):
	# Generate random indices
	randInd1 = random.randint(0, 25)
	randInd2 = random.randint(0, 25)
	while (randInd1 == randInd2):
		randInd2 = random.randint(0, 25)

	# Perform the swap
	keys = list(subTable.keys())
	values = list(subTable.values())
	temp = values[randInd1]
	values[randInd1] = values[randInd2]
	values[randInd2] = temp

	# Update the substitution table
	subTable = dict(zip(keys, values))
	return subTable

# Main
def main():
	# Get user input
	print("Enter the text you want to analyze: ")
	text = input().lower().strip()
	
	# Format text
	# TODO: Keep track of where spaces are removed
	text = text.replace(" ", "")
	text = text.replace("\n", "")
	print(f"Length: {len(text)}")

	# Check if text is a substitution cipher
	ioc = indexOfCoincidence.IndexOfCoincidence(text)
	print(f"Index of Coincidence: {ioc}")
	if (ioc < 0.06):
		print("The text is likely not a substitution cipher.")
		return

	# Generate an initial random substitution table
	subTable = genSubTable()

	# Print the text with the initial substitution table
	subText = substituteText(text, subTable)
	#print(f"Substituted Text: {subText}")
	
	# Perform frequency analysis on the text
	freqDict, letterFrequencies = freqAnalysis.freqAnalysis(subText)
	#print(freqDict)

	# Calculate the expected frequencies
	expectedFrequencies = {}
	sum = 0
	roundedEnglishFrequencies = freqAnalysis.roundFreqs(freqAnalysis.englishFrequencies, 2)
	#print("Expected Frequencies:")
	for letter in freqAnalysis.englishFrequencies:
		expectedFrequencies[letter] = round(roundedEnglishFrequencies[letter] * len(text))
		#print(f"{letter}: {expectedFrequencies[letter]} \t {roundedEnglishFrequencies[letter] * len(text)}")
		sum += expectedFrequencies[letter]
	print(f"Sum: {sum}")
	if (sum != len(text)):
		print("Error: Expected frequencies do not match the length of the text.")
		return

	# Calculate the distance between the frequency of the text and the expected frequency
	fitness = calcFreqDistance(freqDict, expectedFrequencies)
	print(f"Initial Fitness: {fitness}")

	# Perform random swaps and check if the fitness improves
	#iterations = 200000
	while (fitness > 11):
		newSubTable = permute(subTable)
		newSubText = substituteText(text, newSubTable)
		newFreqDict, newLetterFrequencies = freqAnalysis.freqAnalysis(newSubText)
		newFitness = calcFreqDistance(newFreqDict, expectedFrequencies)
		#print(f"New Fitness: {newFitness}")
		if newFitness < fitness:
			#print("Fitness Improved!")
			subTable = newSubTable
			fitness = newFitness
			print(f"New Fitness: {fitness}")

	# Print the final substitution table
	print(f"Final Fitness: {fitness}")
	print("Final Substitution Table:")
	for char in subTable:
		print(f"{char}: {subTable[char]}")
	print("Decoded Text:")
	print(substituteText(text, subTable))
	
# Dunder main
if __name__ == "__main__":
	main()

# Test text: A BCDE CF GHI HAFE CJ KLDGH GKL CF GHI BMJH