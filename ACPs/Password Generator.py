import random
import string

def password_generator(length=15):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    punctuation = string.punctuation

    pas= lower + upper + digits + punctuation

    password = ''.join(random.choice(pas) for _ in range(length))

    return password

password= password_generator(16)
print(password)