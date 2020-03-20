def select_sort(l):
    n = len(l)
    for i in range(n):
        min = i
        for j in range(i+1, n):
            if l[j] < l[min]: min = j
        l[i], l[min] = l[min], l[i]
    return l
list=[6,2,3,7,8,10,21,1]
print(select_sort(list))