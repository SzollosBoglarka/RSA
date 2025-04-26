from fast_exponentiation import fast_exponentiation
from chinese_remainder_theorem import chinese_remainder_theorem

def encrypt(m, e, n):
    return fast_exponentiation(m, e, n)

def decrypt(c, d, p, q):
    return chinese_remainder_theorem(c, d, p, q)