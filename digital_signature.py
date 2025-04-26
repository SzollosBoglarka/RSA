from chinese_remainder_theorem import chinese_remainder_theorem
from fast_exponentiation import fast_exponentiation

def sign(m, d, p, q):
    return chinese_remainder_theorem(m, d, p, q)

def verify(m, s, e, n):
    return m == fast_exponentiation(s, e, n)