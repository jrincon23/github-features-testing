from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file = ".env", extra = "allow")

s = Settings().model_dump()

def validate_odd_positive_integer(number: int):
    """
    Validates that the input is an odd, positive integer.

    Args:
        number (int): The number to validate.

    Raises:
        ValueError: If the input is not an integer, not positive, or not odd.
    """
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
# Generate salt for password hashing
salt = s["salt"].encode()  # Using salt from .env
# Use PBKDF2-HMAC-SHA256 for secure password hashing
strong_hash = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100_000)
# Example of how to store: concatenate hex-encoded salt and hash
stored_password = salt.hex() + ':' + strong_hash.hex()
# Pickle deserialization vulnerability - CodeQL should catch this
import pickle
def load_data(data):
    return pickle.loads(data)  # Unsafe deserialization



