# Harris Ransom
# One-Time Pad Key Generator
# 7/19/2024

# Imports
import secrets
import string
import argparse

# Define key alphabet
alphabet = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation

# Generate a random key of a specified length
def generateKey(length):
    key = []
    for i in range(length):
        key.append(secrets.choice(alphabet))
    return "".join(key)

def generateKeys(length, n):
    keys = []
    for i in range(n):
        keys.append(generateKey(length))
    return keys

# MAIN
def main():
    # Get user input
    parser = argparse.ArgumentParser(description="One-Time Pad Key Generator")
    parser.add_argument("-length", "-l", type=int, help="The length of the key")
    parser.add_argument("-n", "--n", type=int, help="The number of keys to generate")
    args = parser.parse_args()

    # Check user input
    if not args.length:
        print("Please specify the length of the key")
        return
    if not args.n:
        print("Please specify the number of keys to generate")
        return
    if (args.length < 1):
        print("Please specify a key length greater than 0")
        return
    if (args.n < 1):
        print("Please specify a number of keys greater than 0")
        return

    # Generate keys
    keys = generateKeys(args.length, args.n)

    # Print the keys
    for i in range(args.n):
        print(f"{i+1}.) \t {keys[i]}")

# Dunder main
if __name__ == "__main__":
    main()