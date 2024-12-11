import string
import random
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64

def generate_password(length, include_digits, include_special_chars):
    # Define possible character sets
    characters = string.ascii_letters
    if include_digits:
        characters += string.digits
    if include_special_chars:
        characters += string.punctuation

    # Generate a random password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Example usage
try:
    length = int(input("Enter password length (8, 16, 24, 32): "))
    if length not in [8, 16, 24, 32]:
        raise ValueError("Password length must be one of the following: 8, 16, 24, or 32.")
    
    include_digits = input("Include digits? (yes/no): ").lower() == 'yes'
    include_special_chars = input("Include special characters? (yes/no): ").lower() == 'yes'

    # Generate the password
    password = generate_password(length, include_digits, include_special_chars)
    print("Generated password:", password)

except ValueError as e:
    print("Error:", e)