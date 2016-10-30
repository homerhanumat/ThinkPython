def choose(n,k):
    c = 1 if k == 0 else 0 if n == 0 else choose(n-1,k) + choose(n-1,k-1)
    return c

print(choose(10,5))
