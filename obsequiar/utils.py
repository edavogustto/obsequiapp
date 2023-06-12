import random
import string

def generate_sku(length=10):
    characters = string.ascii_uppercase + string.digits
    sku = ''.join(random.choice(characters) for _ in range(length))
    return sku
