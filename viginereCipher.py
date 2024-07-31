# Harris Ransom
# Viginere Cipher Encode/Decode
# 7/28/24

# Imports
import argparse

# Key Generator
def keygen(key, text):
	newKey = list(key)
	if (len(key) == len(text)):
		return key
	else:
		for i in range(len(text) - len(key)):
			newKey.append(key[i % len(key)])
		return "".join(newKey)

# Viginere Cipher Encode
def encode(key, text):
	key = key.upper()
	text = text.upper()
	ciphertext = []
	for i in range(len(text)):
		char = text[i]
		charNum = ord(char) - ord('A')
		keyNum = ord(key[i]) - ord('A')
		sum = (charNum + keyNum) % 26
		ciphertext.append(chr(sum + ord('A')))

	return "".join(ciphertext)

# Viginere Cipher Decode
def decode(key, text):
	key = key.upper()
	text = text.upper()
	plaintext = []
	for i in range(len(text)):
		char = text[i]
		charNum = ord(char) - ord('A')
		keyNum = ord(key[i]) - ord('A')
		diff = (charNum - keyNum) % 26
		plaintext.append(chr(diff + ord('A')))

	return "".join(plaintext)

# MAIN
def main():
	# Parse command line arguments
	parser = argparse.ArgumentParser(description="Viginere Cipher Encode/Decode")
	#parser.add_argument("text", type=str, help="The text you want to encode/decode")
	#parser.add_argument("key", type=str, help="The key")
	parser.add_argument("-e", "--encode", action="store_true", help="Encode the text")
	parser.add_argument("-d", "--decode", action="store_true", help="Decode the text")
	args = parser.parse_args()

	# Get user input
	text = input("Enter the text you want to encode/decode: ").upper().strip()
	key = input("Enter the key: ").upper().strip()

	# Check if the key is shorter than the text
	if (len(key) < len(text)):
		key = keygen(key, text)
		print("Key: " + key)
	
	# Perform encode/decode
	if args.encode:
		ciphertext = encode(key, text)
		print(f"Ciphertext: {ciphertext}")
	elif args.decode:
		plaintext = decode(key, text)
		print(f"Plaintext: {plaintext}")

# Dunder main
if __name__ == "__main__":
	main()