sum = 0
for i in range(1, 101):
    if sum > 1000:
        print(i-1)
        break
    else:
        sum += i
