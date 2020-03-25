list = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]
def merge_sort(l):
    if len(l) < 2: return l
    mid = len(l) // 2
    left = merge_sort(l[:mid])
    right = merge_sort(l[mid:])

    merge_l = []
    i=j=0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merge_l.append(left[i])
            i += 1
        else:
            merge_l.append(right[j])
            j += 1
    merge_l += left[i:]
    merge_l += right[j:]

    return merge_l

print(merge_sort(list))