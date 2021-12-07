p = 17
y = 13
g = 3

print(f'----Field----')
R = GF(p)

print(f'----Solving----')
x = discrete_log(R(y), R(g))

print(f'x = {x}')
#13 (mod 17) = 3 ** 4 