n = int(input("팩토리얼 n : "))
result = 1
def factor(n):
    if n==1: return 1
    return n * factor(n-1)
print(factor(n))