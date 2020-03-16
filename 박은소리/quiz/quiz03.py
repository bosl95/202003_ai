import random
while True:
    i = input("주사위 던지기(enter) 종료(q)")
    if i == 'q': break
    A = random.randint(1,6); B = random.randint(1,6)
    print("A : {}, B : {}".format(A, B))
    if A > B : print("A 승리")
    elif A < B : print("B 승리")
    else: print("동점")

