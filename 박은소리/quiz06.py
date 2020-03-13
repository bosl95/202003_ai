x = int(input("숫자 입력 : "))
for i in range(1, x+1):
    print(("★"*i).center(x))
for i in range(x-1, 0, -1):
    print(("★" * i).center(x))