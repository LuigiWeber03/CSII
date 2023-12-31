def offspringPr(K, N, P = 0.25):
    from scipy.stats import binom 
    prob = 0
    for i in range(N, 2**K + 1):
        prob += binom.pmf(n = 2**K, k = i, p = P)
    return(round(prob, 3))
