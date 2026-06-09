import pytest
from Random_Password_Generator import generate_random_string  # pyright: ignore[reportMissingImports]

def test_password_length_8():
    password = generate_random_string(8)
    assert len(password) == 8

def test_password_length_20():
    password = generate_random_string(20)
    assert len(password) == 20

def test_password_is_string():
    password = generate_random_string(10)
    assert isinstance(password, str)

def test_password_contains_only_valid_characters():
    valid_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    password = generate_random_string(15)

    for char in password:
        assert char in valid_chars

def test_zero_length_password():
    password = generate_random_string(0)
    assert password == ""

def test_negative_length_password():
    password = generate_random_string(-5)
    assert password == ""
