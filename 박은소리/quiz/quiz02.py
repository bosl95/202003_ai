x, y, cal = input("첫번째 수, 두번째 수 , 연산 기호 : ").split()
x = int(x); y=int(y)
if cal == '+':
    print(x+y)
elif cal == '-':
    print(x-y)
elif cal == '/':
    print(x/y)
else:
    print(x%y)