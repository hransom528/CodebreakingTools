# Harris Ransom
# One-Time Pad Cipher - Vernam Cipher Implementation
# 7/19/2024

# Imports
import secrets
import string
import argparse

# Generate a random key of a specified length
def generateKey(length):
    key = []
    for i in range(length):
        key.append(secrets.choice(string.ascii_uppercase))
    return "".join(key)

# Encrypt plaintext using a one-time pad
# Decrypt ciphertext using a one-time pad
def vernamCipher(plaintext, key):
    ciphertext = bytearray()
    plaintextBytes = bytes(plaintext, "utf-8")
    keyBytes = bytes(key, "utf-8")
    for i in range(len(plaintext)):
        character = plaintextBytes[i] ^ keyBytes[i]
        ciphertext.append(character)
    return ciphertext

# MAIN
def main():
    # Get user input
    #parser = argparse.ArgumentParser(description="One-Time Pad Cipher")
    #parser.add_argument("mode", help="Encrypt or decrypt")
    #args = parser.parse_args()

    plaintext = input("Enter text to encrypt: ").upper()
    plaintext = plaintext.strip()

    # Generate a key of the same length as the plaintext
    key = generateKey(len(plaintext))
    print(f"Key: {key}")

    # Encrypt the plaintext
    ciphertext = vernamCipher(plaintext, key)
    print(f"Ciphertext: {ciphertext}")

# Dunder main
if __name__ == "__main__":
    main()