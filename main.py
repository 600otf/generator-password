import string
import random
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64

def generate_password(length, include_digits, include_special_chars):
    # Définir les ensembles de caractères possibles
    characters = string.ascii_letters
    if include_digits:
        characters += string.digits
    if include_special_chars:
        characters += string.punctuation

    # Générer un mot de passe aléatoire
    password = ''.join(random.choice(characters) for i in range(length))

    # S'assurer que la longueur du mot de passe est de 16 octets pour le chiffrement
    if len(password) < 16:
        password = password.ljust(16)  # Compléter le mot de passe à 16 octets
    else:
        password = password[:16]  # Tronquer le mot de passe à 16 octets

    # Chiffrer le mot de passe
    key = get_random_bytes(32)  # AES-256 nécessite une clé de 32 octets
    cipher = AES.new(key, AES.MODE_ECB)
    password_bytes = password.encode()
    encrypted_password = cipher.encrypt(password_bytes)
    encoded_password = base64.b64encode(encrypted_password).decode('utf-8')

    return encoded_password

# Exemple d'utilisation
length = int(input("Enter password length (8, 16, 24, 32): "))
include_digits = input("Include digits? (yes/no): ").lower() == 'yes'
include_special_chars = input("Include special characters? (yes/no): ").lower() == 'yes'

print("Generated password:", generate_password(length, include_digits, include_special_chars))