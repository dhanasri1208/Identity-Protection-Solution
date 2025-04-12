import hashlib
import requests

# Function to generate a SHA-1 hash of a given password (HIBP uses SHA-1, not SHA-256)
def generate_hash(password):
    return hashlib.sha1(password.encode('utf-8')).hexdigest().upper()

# Function to check if a password has been compromised in a data breach
def check_compromised_password(password):
    sha1_hash = generate_hash(password)
    hash_prefix = sha1_hash[:5]
    hash_suffix = sha1_hash[5:]
    
    url = f'https://api.pwnedpasswords.com/range/{hash_prefix}'
    response = requests.get(url)
    
    if response.status_code != 200:
        raise RuntimeError(f"API request failed: {response.status_code}")
    
    hashes = response.text.splitlines()
    for line in hashes:
        suffix, count = line.split(":")
        if suffix == hash_suffix:
            return True  # Found in the breach list
    return False

# Function to validate a user's password
def validate_password(username, password):
    if len(password) < 8:
        return False, "Password must be at least 8 characters long"
    if username.lower() in password.lower():
        return False, "Password cannot contain the username"
    if check_compromised_password(password):
        return False, "Password has been compromised in a data breach"
    return True, "Password is valid"

# Example usage
username = "admin"
password = "password"
is_valid, message = validate_password(username, password)

print(message)
