def is_strong_password(pwd):
    if len(pwd) < 8:
        return False
    if not any(c.isupper() for c in pwd):
        return False
    if not any(c.islower() for c in pwd):
        return False
    if not any(c.isdigit() for c in pwd):
        return False
    if not any(c in "@#_!-?$%&()[]{}" for c in pwd):
        return False
    return True