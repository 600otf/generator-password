import string
import random
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

# --- Color codes for display ---
RED = "\33[91m"
BLUE = "\33[94m"
GREEN = "\033[32m"
YELLOW = "\033[93m"
PURPLE = '\033[0;35m'
CYAN = "\033[36m"
END = "\033[0m"

# --- Banner ---
BANNER = f"""
{PURPLE}
  ____    ___  ____     ___  ____    ____  ______   ___   ____       ____    ____   _____ _____ __    __   ___   ____   ___   
 /    |  /  _]|    \   /  _]|    \  /    ||      | /   \ |    \     |    \  /    | / ___// ___/|  |__|  | /   \ |    \ |   \  
|   __| /  [_ |  _  | /  [_ |  D  )|  o  ||      ||     ||  D  )    |  o  )|  o  |(   \_(   \_ |  |  |  ||     ||  D  )|    \ 
|  |  ||    _]|  |  ||    _]|    / |     ||_|  |_||  O  ||    /     |   _/ |     | \__  |\__  ||  |  |  ||  O  ||    / |  D  |
|  |_ ||   [_ |  |  ||   [_ |    \ |  _  |  |  |  |     ||    \     |  |   |  _  | /  \ |/  \ ||  `  '  ||     ||    \ |     |
|     ||     ||  |  ||     ||  .  \|  |  |  |  |  |     ||  .  \    |  |   |  |  | \    |\    | \      / |     ||  .  \|     |
|___,_||_____||__|__||_____||__|\_||__|__|  |__|   \___/ |__|\_|    |__|   |__|__|  \___| \___|  \_/\_/   \___/ |__|\_||_____|   
{END}
"""
print(BANNER)

# --- Secure password generator ---
def generate_password(length=16, include_digits=True, include_special_chars=True):
    """Generates a secure random password."""
    # [MODIFIED] - Added AES-compatible key length check
    if length not in [8, 16, 24, 32]:
        raise ValueError("Length must be 8, 16, 24, or 32 characters (AES key size).")

    # [MODIFIED] - Reorganized character set logic for readability
    characters = string.ascii_letters
    if include_digits:
        characters += string.digits
    if include_special_chars:
        characters += string.punctuation

    # [MODIFIED] - Use SystemRandom for cryptographically secure randomness
    secure_random = random.SystemRandom()
    password = ''.join(secure_random.choice(characters) for _ in range(length))
    return password


def main():
    """Main user interaction loop."""
    try:
        # [MODIFIED] - Added clear user interface and color output
        print(f"{CYAN}--- Secure Password Generator ---{END}")
        length = int(input("Password length (8, 16, 24, 32): ").strip())
        include_digits = input("Include digits? (y/n): ").lower().startswith('y')
        include_special_chars = input("Include special characters? (y/n): ").lower().startswith('y')

        # [MODIFIED] - Generate password with user options
        password = generate_password(length, include_digits, include_special_chars)

        # [MODIFIED] - Improved colored output and length display
        print(f"\n{GREEN}Generated password:{END} {YELLOW}{password}{END}")
        print(f"{BLUE}Length:{END} {len(password)} characters\n")

    except ValueError as e:
        print(f"{RED}Error: {e}{END}")


# [MODIFIED] - Added main entry point for better structure
if __name__ == "__main__":
    main()
