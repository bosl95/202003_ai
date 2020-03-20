def bubble_sort(l):
    n = len(l)
    for i in range(n-1, 0, -1):
        for j in range(i):
            if l[j] > l[j+1]: l[j+1], l[j] = l[j], l[j+1]
    return l

list=[4,3,2,1,8,7,5,10,11,16,21,6]

print(bubble_sort(list))