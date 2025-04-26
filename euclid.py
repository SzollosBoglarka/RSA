def euclid(a, b):
    while b != 0:
        d = a
        a = b
        b = d % a

    return a

#print(euclid(80, 50))