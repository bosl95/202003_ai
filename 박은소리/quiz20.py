for i in range(1, 101):
    s = str(i)
    if '3' in s or '6' in s or '9' in s:
        print("짝")
    elif i%5==0:
        print("아자")
    else:
        print(i)