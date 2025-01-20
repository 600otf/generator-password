import string
import random
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64

import string


RED = "\33[91m"
BLUE = "\33[94m"
GREEN = "\033[32m"
YELLOW = "\033[93m"
PURPLE = '\033[0;35m' 
CYAN = "\033[36m"
END = "\033[0m"

banner =f"""

{PURPLE}

  ____    ___  ____     ___  ____    ____  ______   ___   ____       ____    ____   _____ _____ __    __   ___   ____   ___   
 /    |  /  _]|    \   /  _]|    \  /    ||      | /   \ |    \     |    \  /    | / ___// ___/|  |__|  | /   \ |    \ |   \  
|   __| /  [_ |  _  | /  [_ |  D  )|  o  ||      ||     ||  D  )    |  o  )|  o  |(   \_(   \_ |  |  |  ||     ||  D  )|    \ 
|  |  ||    _]|  |  ||    _]|    / |     ||_|  |_||  O  ||    /     |   _/ |     | \__  |\__  ||  |  |  ||  O  ||    / |  D  |
|  |_ ||   [_ |  |  ||   [_ |    \ |  _  |  |  |  |     ||    \     |  |   |  _  | /  \ |/  \ ||  `  '  ||     ||    \ |     |
|     ||     ||  |  ||     ||  .  \|  |  |  |  |  |     ||  .  \    |  |   |  |  | \    |\    | \      / |     ||  .  \|     |
|___,_||_____||__|__||_____||__|\_||__|__|  |__|   \___/ |__|\_|    |__|   |__|__|  \___| \___|  \_/\_/   \___/ |__|\_||_____|  """
                                                                                                                              

print(banner)
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