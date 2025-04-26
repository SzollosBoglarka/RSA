from random import randint
from miller_rabin import is_prime

def prime_generation():
    p = randint(100, 10000)
    while is_prime(p) != "Probably Prime":
        p = randint(100, 10000)

    return p

#print(is_prime(prime_generation()))