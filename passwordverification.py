def check_password_strength(password):
    """
    Verifies if a password meets the required strength criteria:
    - More than 8 characters
    - At least one uppercase letter
    - At least one lowercase letter
    - At least one number
    """
    
    # Initialize criteria checks
    length_ok = len(password) > 8
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_number = any(char.isdigit() for char in password)
    
    # Print results
    print("\n" + "="*50)
    print("PASSWORD STRENGTH VERIFICATION")
    print("="*50)
    print(f"Password: {'*' * len(password)}")
    print(f"Length: {len(password)} characters")
    print("-"*50)
    
    print(f"✓ More than 8 characters: {'PASS' if length_ok else 'FAIL'} ({len(password)} characters)")
    print(f"✓ Contains uppercase letter: {'PASS' if has_upper else 'FAIL'}")
    print(f"✓ Contains lowercase letter: {'PASS' if has_lower else 'FAIL'}")
    print(f"✓ Contains at least one number: {'PASS' if has_number else 'FAIL'}")
    print("-"*50)
    
    # Overall result
    password_is_strong = length_ok and has_upper and has_lower and has_number
    
    if password_is_strong:
        print("RESULT: ✓ PASSWORD IS STRONG ENOUGH")
    else:
        print("RESULT: ✗ PASSWORD IS NOT STRONG ENOUGH")
        print("\nNeeded improvements:")
        if not length_ok:
            print(f"  - Make password longer (need {9 - len(password)} more characters)")
        if not has_upper:
            print("  - Add at least one uppercase letter (A-Z)")
        if not has_lower:
            print("  - Add at least one lowercase letter (a-z)")
        if not has_number:
            print("  - Add at least one number (0-9)")
    
    print("="*50 + "\n")
    
    return password_is_strong


# Main program
if __name__ == "__main__":
    while True:
        password = input("Enter a password to verify (or 'quit' to exit): ")
        
        if password.lower() == 'quit':
            print("Goodbye!")
            break
        
        if len(password) == 0:
            print("Password cannot be empty. Please try again.\n")
            continue
        
        check_password_strength(password)
