import random
import string

def generate_password(min_length, numbers=True, special_characters=True):
    
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation 

    characters = letters
    if numbers:
        characters += digits
    if special_characters:
        characters += special
    
    pwd = ""
    meets_criteria = False
    has_number = False
    has_special = False

    while not meets_criteria or len(pwd) < min_length:
        new_char = random.choice(characters)
        pwd += new_char

        if new_char in digits:
            has_number = True
        if new_char in special:
            has_special = True

        meets_criteria = True
        if numbers:
            meets_criteria = has_number
        if special_characters:
            meets_criteria = meets_criteria and has_special
    return pwd

    
min_length = int(input("Enter the minimum length of the password: "))
has_number = input("Include numbers? (y/n): ").lower() == 'y'
has_special = input("Include special characters? (y/n): ").lower() == 'y'

pwd = generate_password(min_length, has_number, has_special)
print(f"Generated password: {pwd}")
# This script generates a random password based on user-defined criteria.

