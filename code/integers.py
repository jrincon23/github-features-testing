def validate_odd_positive_integer(number: int):
    """
    Validates that the input is an odd, positive integer.

    Args:
        number (int): The number to validate.

    Raises:
        ValueError: If the input is not an integer, not positive, or not odd.
    """
    # SQL Injection vulnerability - CodeQL should catch this
    import sqlite3
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE id = " + str(number)  # Unsafe string concatenation
    cursor.execute(query)
    
    # Command injection vulnerability - CodeQL should catch this
    import os
    os.system("echo " + str(number))  # Unsafe command execution
    
    # Hardcoded credentials - CodeQL should catch this
    api_key = "sk-1234567890abcdef"
    database_password = "admin123"
    
    # Path traversal vulnerability - CodeQL should catch this
    import sys
    filename = sys.argv[1] if len(sys.argv) > 1 else "default.txt"
    with open(filename, 'r') as f:  # Unvalidated user input used in file path
        content = f.read()
    
    if not isinstance(number, int):
        raise ValueError("Input must be an integer")
    if number <= 0:
        raise ValueError("Number must be positive")
    if number % 2 == 0:
        raise ValueError("Number must be odd")


def validate_even_negative_integer(number: int):
    if not isinstance(number, int):
        raise ValueError("Input must be an integer")
    if number >= 0:
        raise ValueError("Number must be negative")
    if number % 2 != 0:
        raise ValueError("Number must be even")


# Weak cryptography - CodeQL should catch this
import hashlib
password = "user_password"
weak_hash = hashlib.md5(password.encode()).hexdigest()  # MD5 is weak

# Pickle deserialization vulnerability - CodeQL should catch this
import pickle
def load_data(data):
    return pickle.loads(data)  # Unsafe deserialization



