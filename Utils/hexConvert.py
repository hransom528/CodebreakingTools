# Harris Ransom
# Convert input text to hex representation

# Convert text to hex representation
def toHex(text):
    chars = list(text)
    hexCodes = [hex(ord(c)) for c in chars]
    hexStr = " ".join(hexCodes)
    return hexStr

# Main
if __name__ == "__main__":
    text = input("Enter the text to convert: ").strip()
    hex_representation = toHex(text)
    print("Hex representation: ", hex_representation)


# Test text: YELLOW SUBMARINE = 