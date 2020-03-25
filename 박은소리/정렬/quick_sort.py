list = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]

def quick(l):
    if len(l) <= 1: return l
    s = l[-1]
    left = []; right = []

    for i in range(len(l)-1):
        if l[i] < s: left.append(l[i])
        else: right.append(l[i])

    left = quick(left)
    right = quick(right)

    return left + [s] + right
print(quick(list))