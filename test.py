import random

def generate_random_digits():
    digits = []
    for _ in range(6):
        digit = random.randint(0, 9)
        digits.append(str(digit))
    
    return ''.join(digits)

random_digits = generate_random_digits()
print(random_digits)
