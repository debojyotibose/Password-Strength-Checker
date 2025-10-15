def check_strength(password):
    strength = 0
    # Criteria checks
    if len(password) >= 8:
        strength += 1
    if any(char.isdigit() for char in password):
        strength += 1
    if any(char.islower() for char in password):
        strength += 1
    if any(char.isupper() for char in password):
        strength += 1
    if any(char in "!@#$%^&*()-_=+[]{}|;:'\",.<>?/~`" for char in password):
        strength += 1
    return strength

def print_suggestions(password):
    if len(password) < 8:
        print("Try to use at least 8 characters.")
    if not any(char.isdigit() for char in password):
        print("Add some digits to your password.")
    if not any(char.islower() for char in password):
        print("Add lowercase letters.")
    if not any(char.isupper() for char in password):
        print("Add uppercase letters.")
    if not any(char in "!@#$%^&*()-_=+[]{}|;:'\",.<>?/~`" for char in password):
        print("Add special characters (like !, @, #, etc.).")

print("Password Strength Checker")
print("Type 'exit' to quit.\n")

while True:
    password = input("Enter your password: ")
    if password.lower() == 'exit':
        print("Session ended.")
        break
    if not password.strip():
        print("Password cannot be empty!\n")
        continue
    
    strength = check_strength(password)
    if strength <= 2:
        print("Weak password")
    elif strength == 3:
        print("Medium strength password")
    else:
        print("Strong password")
    
    print_suggestions(password)
    print()  # For spacing
