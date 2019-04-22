import random


def create_random_str(n):
    s = 'QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890'
    random_str = ''
    for i in range(n):
        random_str += random.choice(s)
    return random_str