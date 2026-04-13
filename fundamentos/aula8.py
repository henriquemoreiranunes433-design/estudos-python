def fatorial(n, show = True):
    f = 1
    for c in range (n , 0, -1):
        f *= c
    return f


print(fatorial(5))