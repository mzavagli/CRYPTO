from sympy import mod_inverse

"""
Cinese remainder theorem : 

Let n be a random number

If you have m remainders of euclidian divisions of n with m integers, 
then you can retrieve n if those m integers are pairwise coprime.

x = dlogs[0] (mod n[0])
x = dlogs[1] (mod n[1])
...
x = dlogs[m-1] (mod n[m-1])

N = n[0] * n[1] * ... * n[m-1]

Ni = N // ni

xi = mod_inverse(Ni, ni)

x = (x0 * N0 * dlogs[0]) + ... + (xm-1 * Nm-1 * dlogs[m-1])
"""

def check_size(a, b):
    return (dlogs) == len(n_list)

# Classic version
def solve_crt_n(dlogs, n_list):

    if not check_size:
        return -1

    n = 1
    for i in n_list:
        n *= i
    # print n
    x = 0
    for i in range(len(dlogs)):
        Ni = n // (n_list[i])
        # print Ni
        xi = mod_inverse(Ni, (n_list[i]))
        # print xi
        x += dlogs[i] * Ni * xi
    return x % n

# Factor version (for discrete log attacks)
# factors = [(a0, b0), ..., (an, bn)] such that (for example with PohligHellman) p-1 = (a0 ** b0) * ... * (an ** bn)
def solve_crt_f(dlogs, factors):

    if not check_size:
        return -1

    n = 1
    for i in factors:
        n *= (i[0]**i[1])
    # print n
    x = 0
    for i in range(len(dlogs)):
        Ni = n // (factors[i][0]**factors[i][1])
        # print yi
        xi = mod_inverse(Ni, (factors[i][0]**factors[i][1]))
        # print zi
        x += dlogs[i] * Ni * xi
    return x % n

def main():
    dlogs = [3, 1, 6]
    n_list = [5, 7, 8]

    print(solve_crt_n(dlogs, n_list))
    # 78 = 3 (mod 5)
    # 78 = 1 (mod 7)
    # 78 = 6 (mod 8)


if __name__ == "__main__":
    main()