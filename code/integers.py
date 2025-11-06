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


# Strong password hashing using PBKDF2-HMAC-SHA256
import hashlib
import os
password = "user_password"
# Generate a random salt for password hashing
salt = os.urandom(16)
# Use PBKDF2-HMAC-SHA256 for secure password hashing
strong_hash = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100_000)
# Example of how to store: concatenate hex-encoded salt and hash
stored_password = salt.hex() + ':' + strong_hash.hex()
# Pickle deserialization vulnerability - CodeQL should catch this
import pickle
def load_data(data):
    return pickle.loads(data)  # Unsafe deserialization



