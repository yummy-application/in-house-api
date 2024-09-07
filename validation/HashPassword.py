import hashlib


def md5(password:str):
    return hashlib.md5(password.encode()).hexdigest()