import random
import string


def generate_password(lenght=12):
    """Generate a strong Password of specified leght (default 12)"""
    characters = string.ascii_letters + string.digits + string.punctuation
    password = []


# ensure atleat one of each character type
