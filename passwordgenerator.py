import random
import string

def generate_password(length=12):
    """
    Generates a strong, random password of a specified length.

    The password includes a mix of:
    - Lowercase letters
    - Uppercase letters
    - Digits
    - Punctuation (symbols)
    """
    if length < 4:
        # Ensure the password is long enough to include one of each type
        print("Warning: Password length should be at least 4 to ensure complexity.")
        length = 4

    # 1. Define the character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    # Combine all characters that can be used
    all_characters = lowercase + uppercase + digits + symbols

    # 2. Ensure the password has at least one of each type for strength
    password = []
    password.append(random.choice(lowercase))
    password.append(random.choice(uppercase))
    password.append(random.choice(digits))
    password.append(random.choice(symbols))

    # 3. Fill the remaining length with random choices from all characters
    # We already used 4 characters, so we loop for the remaining length
    remaining_length = length - 4
    for _ in range(remaining_length):
        password.append(random.choice(all_characters))

    # 4. Shuffle the list to ensure the required characters aren't always at the start
    random.shuffle(password)

    # 5. Join the list of characters into a single string
    return "".join(password)

def main():
    """
    Main function to handle user input and display the generated password.
    """
    print("--- Strong Password Generator ---")
    
    while True:
        try:
            # Get the desired password length from the user
            length = int(input("Enter the desired password length (e.g., 12 or 16): "))
            if length <= 0:
                print("Please enter a positive length.")
                continue
            
            # Generate and print the password
            password = generate_password(length)
            print("\nGenerated Password: ")
            print(f"==========================================")
            print(f"| {password} |")
            print(f"==========================================")
            break
        except ValueError:
            print("Invalid input. Please enter a whole number.")
            
if __name__ == "__main__":
    main()