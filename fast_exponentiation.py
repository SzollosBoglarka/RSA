def fast_exponentiation(base, exp, mod):
    result = 1

    while exp > 0:
        if exp % 2 == 1:
            result = (base * result) % mod
        base = (base * base) % mod
        exp = exp // 2

    return result

#print(fast_exponentiation(6, 73, 100))