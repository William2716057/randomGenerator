import random
import string

def generate_random_string(length=8):
    characters = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(characters) for i in range(length))
    return random_string

# Generate random string
random_string = generate_random_string()
print(random_string)

# Encode string to bytes and then back to string to avoid b'...'
sample_bytes = random_string.encode("ascii")
print(sample_bytes)
decoded_string = sample_bytes.decode("ascii")
print(decoded_string)

# Print result as an email address
print(f"{decoded_string}@outlook.com")