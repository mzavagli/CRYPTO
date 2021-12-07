"""
RSA decrypt bc I tired of writting this same exact shit again and again in each CTF
"""

from binascii import hexlify, unhexlify, Error
from random import randint

def calculate_n(p, n):
    return p * q

def calculate_d(phi, e):
    return pow(e, -1, phi)

def calculate_phi(p, q):
    return (p - 1) * (q - 1)

def decrypt(ct, d, n):
    return pow(ct, d, n)

def encrypt(pt, e, n):
    return pow(pt, e, n)

def int_to_latin(pt):
    return unhexlify(hex(pt)[2:]).decode("latin")

def main():

    FILENAME = "flag.enc"

    # None if you don't have it
    # int or hex (0x format)
    n = 0x219C75AEE23AEE202503EC5025B40AC9E18C546E6EF1965B4B
    p = 411481484074428595727757344849
    q = 512734463417573692484064589531
    e = 7
    
    ct = 8711853753483579701322290941915765213212086928701373860451
    
    d = None  # 0x04cd356220518fbb73008f79284a88c0ea3ee05718c119e097
    
    if n is None:
        n = calculate_n(p, q)

    if d is None:
        phi = calculate_phi(p, q)
        d = calculate_d(phi, e)

    assert (e * d) % phi == 1

    
    print(
        f"> p : {p}\n> q : {q}\n> n : {n}\n> d : {d}\n> e : {e}\n> phi : {phi}"
    )

    # private key test
    test_pt = randint(1, n)
    test_ct = encrypt(test_pt, e, n)
    assert decrypt(test_ct, d, n) == test_pt

    # read file
    if ct is None:
        with open(FILENAME, "rb") as infile:
            ct = infile.read()
            ct = int(hexlify(ct), 16)
    
    pt_int = decrypt(ct, d, n)
    
    try:
        pt = int_to_latin(pt_int)  # if odd-string length -> add '0' in front of the hex
    except Error:
        print(f"Probably odd-length hex")

    print("---------------- RESULTS ----------------")    
    print(pt)


if __name__ == "__main__":
    main()
