from fast_exponentiation import fast_exponentiation
from random import randint

def is_strong_pseudoprime(n, a):
    d = n - 1
    s = 0

    while d % 2 == 0:
        d /= 2
        s += 1

    t = fast_exponentiation(a, d, n)
    if t == 1 or t == n - 1:
        return "Probably Prime"

    while s > 0:
        t = (t * t) % n
        if t == n-1:
            return "Probably Prime"
        s -= 1

    return "Composite"

def is_prime(n, k=8):
    for i in range(1, k):
        a = randint(2, n-1)
        if is_strong_pseudoprime(n, a) == "Composite":
            return "Composite"
    return "Probably Prime"

#print(is_prime(454))