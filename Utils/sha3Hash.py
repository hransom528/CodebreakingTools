# Harris Ransom
# SHA-3 Hashing Algorithm
# 8/3/2024

# Imports
from hashlib import sha3_512
import argparse

# MAIN
if __name__ == "__main__":
    # Get user input
    message = input("Enter the message to hash: ").strip()
    #parser = argparse.ArgumentParser(description='SHA-3 Hashing Algorithm')
    #parser.add_argument('message', type=str, help='The message to hash')
    #parser.add_argument('-n', '--n', type=int, help='The number of hashing bits')
    #args = parser.parse_args()

    # Hash the message using SHA-3
    hashed_message = sha3_512(message.encode()).hexdigest()

    # Print the hashed message
    print("Hashed message:", hashed_message)