

def calculate_discount(price, user_type):
    """Calculate the discounted price based on user type."""
    DISCOUNT_RATES = {
        "regular": 0.05,
        "premium": 0.10,
        "vip": 0.25
    }
    if user_type not in DISCOUNT_RATES:
        raise ValueError(f"Invalid user type: {user_type}")

    discount = DISCOUNT_RATES[user_type]
    return price * (1 - discount)