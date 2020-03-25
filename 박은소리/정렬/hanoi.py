def print_hanoi(n, a, b):
    print("{}번 기둥의 {}번 원반을 {}번 기둥에 옮긴다.".format(a, n, b))
def hanoi(n, a, b):
    if n:
        hanoi(n-1, a, 6-a-b)
        print_hanoi(n, a, b)
        hanoi(n-1, 6-a-b, b)
hanoi(3, 1, 3)

'''
1. 기둥 1에서 N-1개의 원반을 기둥 3을 이용해 기둥 2로 옮김
2. 기둥 1에서 1개의 원반을 기둥 3으로 옮김
3. 기둥 2에서 N-1개의 원반을 기둥 1을 이용해 기둥 3으로 옮김
'''