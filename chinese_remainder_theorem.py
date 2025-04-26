from fast_exponentiation import fast_exponentiation
from extended_euclid import extended_euclid

def chinese_remainder_theorem(c, d, p, q):
    c1 = fast_exponentiation(c, d % (p-1), p)
    c2 = fast_exponentiation(c, d % (q-1), q)

    M = p*q
    M1 = q
    M2 = p

    (gcd, y1, y2) = extended_euclid(M1, M2)

    m = (c1*M1*y1 + c2*M2*y2) % M

    while m < 0:
        m += M

    return m

#print(chinese_remainder_theorem(15, 23, 5, 11))