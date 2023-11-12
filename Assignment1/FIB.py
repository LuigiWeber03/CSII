//code for the FIB exercise, from the Rosalind website
n = 
k = 

def rabbit_pairs(n, k):
    pairs = [1, 1]
    for i in range(2, n):
        new_pairs = pairs[i - 1] + k * pairs[i - 2]
        pairs.append(new_pairs)
    return pairs[n - 1]
print(rabbit_pairs(n, k))
