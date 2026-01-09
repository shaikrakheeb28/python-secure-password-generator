# password_generator.py

import random
import string

class PasswordGenerator:
    def __init__(self, length=12, use_uppercase=True, use_digits=True, use_specials=True):
        self.length = length
        self.use_uppercase = use_uppercase
        self.use_digits = use_digits
        self.use_specials = use_specials

    def generate(self):
        characters = list(string.ascii_lowercase)
        if self.use_uppercase:
            characters += list(string.ascii_uppercase)
        if self.use_digits:
            characters += list(string.digits)
        if self.use_specials:
            characters += list("!@#$%^&*()-_=+[]{}|;:,.<>?")

        if not characters:
            raise ValueError("No character sets selected.")

        password = ''.join(random.choice(characters) for _ in range(self.length))
        return password

def main():
    print("=== Password Generator ===")
    try:
        length = int(input("Enter desired password length (default 12): ") or 12)
        use_uppercase = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
        use_digits = input("Include digits? (yes/no): ").lower() == 'yes'
        use_specials = input("Include special characters? (yes/no): ").lower() == 'yes'

        generator = PasswordGenerator(length, use_uppercase, use_digits, use_specials)
        password = generator.generate()
        print(f"Generated Password: {password}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
