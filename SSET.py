import math
from scipy.special import comb, perm

with open("rosalind_sset.txt", "r") as f:
    n = int(f.readline().strip())
print(n)

s = 0
for i in range(1, n+1):
    s += int(math.factorial(n) / (math.factorial(i) * math.factorial(n-i)))
print(s)
print(s%1000000)