"""
Because I'm f*cking tired of those scripts that don't work
"""

from binascii import hexlify, unhexlify, Error
from random import randint


class RSAObj:
    def __init__(self, p=None, q=None, n=None, d=None, e=0x10001):
        # Fill up info there ma caille
        self.p = p
        self.q = q
        self.n = n
        self.d = d
        self.phi = None
        self.e = e

    def calculate_n(self):
        if (self.p is not None) and (self.q is not None):
            self.n = self.p * self.q

    def calculate_d(self):
        if (self.phi is not None) and (self.e is not None):
            self.d = pow(self.e, -1, self.phi)

    def calculate_phi(self):
        if (self.q is not None) and (self.p is not None):
            self.phi = (self.p - 1) * (self.q - 1)

    def display_info(self):
        print(
            f"> p : {self.p}\n> q : {self.q}\n> n : {self.n}\n> d : {self.d}\n> e : {self.e}\n> phi : {self.phi}"
        )

    def decrypt(self, c):
        return pow(c, self.d, self.n)

    def encrypt(self, p):
        return pow(p, self.e, self.n)

    def int_to_latin(self, p):
        return unhexlify(hex(p)[2:]).decode("latin")


def main():

    FILENAME = "flag.enc"

    # None if you don't have it
    # int or hex (0x format)
    n = 0x219C75AEE23AEE202503EC5025B40AC9E18C546E6EF1965B4B
    p = 411481484074428595727757344849
    q = 512734463417573692484064589531
    d = None  # 0x04cd356220518fbb73008f79284a88c0ea3ee05718c119e097
    e = 7

    c = 8711853753483579701322290941915765213212086928701373860451

    rsa = RSAObj(p, q, n, d, e)

    # check private key presence
    if ((rsa.p is None) or (rsa.q is None)) and (rsa.d is None):
        print("Not enougth info")
        return 0

    if rsa.n is None:
        if (rsa.p is None) or (rsa.q is None):
            print("Not enougth info")
            return 0
        else:
            rsa.calculate_n()

    if rsa.d is None:
        rsa.calculate_phi()
        rsa.calculate_d()

    assert (rsa.e * rsa.d) % rsa.phi == 1

    rsa.display_info()

    # private key test
    test_p = randint(1, rsa.n)
    test_c = rsa.encrypt(test_p)
    assert rsa.decrypt(test_c) == test_p

    # read file
    if c is None:
        with open(FILENAME, "rb") as infile:
            c = infile.read()
            c = int(hexlify(c), 16)

    # decrypt
    p = rsa.int_to_latin(rsa.decrypt(c))

    print("---------------- RESULTS ----------------")
    try:
        print(p)  # if odd-string length -> add '0' in front of the hex
    except Error:
        print(f"Probably odd-length hex")


if __name__ == "__main__":
    main()
