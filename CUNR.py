from functools import reduce

def cunr(n, mod=10**6):
    return reduce(lambda a, b: a * b % mod, range(2 * n - 5, 1, -2))
print(cunr(int(n)))