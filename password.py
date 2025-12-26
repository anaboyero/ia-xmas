# Critique:
# - The password rules (such as minimum length and special characters) are hardcoded throughout the function.
#   This makes it tedious to update the rules later.
# - The error returns are generic and provide no indication of which password rule was violated. 
# - The use of inline string for special characters is easy to mistype or update inconsistently.
# - The code has repeated patterns which could be extracted or clarified for easier extension.
# - The function lacks documentation.
#
# Recommendations:
# - Define constants for the password requirements (such as MIN_LENGTH, SPECIAL_CHARS).
# - Optionally, consider returning more detailed error information for future extensibility.
# - Add a docstring to clarify the password policy.
# - Cluster the rules in a way that’s easier to expand or change.
#
# Example improved code:
MIN_LENGTH = 8
SPECIAL_CHARS = "@#_!-?$%&()[]{}"
def is_strong_password(pwd):
    """
    Returns a list of password rule violations. If the list is empty, the password is strong.
     - At least MIN_LENGTH characters
     - Contains at least one uppercase letter
     - Contains at least one lowercase letter
     - Contains at least one digit
     - Contains at least one special character from SPECIAL_CHARS
    """
    errors = []
    if len(pwd) < MIN_LENGTH:
        errors.append(f"Password is too short. You need at least {MIN_LENGTH} characters")
    if not any(c.isupper() for c in pwd):
        errors.append("Password does not contain an uppercase letter")
    if not any(c.islower() for c in pwd):
        errors.append("Password does not contain a lowercase letter")
    if not any(c.isdigit() for c in pwd):
        errors.append("Password does not contain a digit")
    if not any(c in SPECIAL_CHARS for c in pwd):
        errors.append(f"Password does not contain a special character. You need to use at least one of the following characters: {SPECIAL_CHARS}")
    return errors
