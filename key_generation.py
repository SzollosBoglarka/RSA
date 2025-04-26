from random import randint
from euclid import euclid
from extended_euclid import extended_euclid

def key_generation(p, q):
    n = p * q
    phi_n = (p-1)*(q-1)

    e = 0
    while True:
        e = randint(2, phi_n)
        if euclid(phi_n, e) == 1:
            break

    d = extended_euclid(phi_n, e)[2]
    while d < 0:
        d += phi_n

    return d, e, n