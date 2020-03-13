def GCD(a, b):
    if a < b: a, b = (b, a)
    while b != 0:
        (a, b) = (a, a%b)
    return a

print(GCD(3, 36))