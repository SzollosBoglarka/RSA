from digital_signature import sign, verify
from key_generation import key_generation
from prime_generation import prime_generation
from rsa import encrypt, decrypt

def main():
    print("RSA")
    m = int(input("Message: "))
    p = prime_generation()
    q = prime_generation()
    while p == q:
        q = prime_generation()

    d, e, n = key_generation(p, q)

    print(f"public key (e,n): ({e}, {n}); secret key (d,n): ({d}, {n})")

    c = encrypt(m, e, n)
    print("Encryption")
    print(f"c: {c}")

    m = decrypt(c, d, p, q)
    print("Decryption")
    print(f"m: {m}")

    print()
    print("Digital Signature")
    m = int(input("Message: "))
    s = sign(m, d, p, q)
    print(f"Signature: {s}")

    m = int(input("Verification: "))
    if verify(m, s, e, n):
        print("Successful verification")
    else:
        print("Unsuccessful verification")

if __name__ == "__main__":
    main()
