m = int(input('액수 입력 : '))
coin = list(map(int, input('동전의 종류 : ').split()))
def greedy():
    global m; result = ''
    for i in range(0, len(coin)):
        tmp = m // coin[i]
        m -= coin[i] * tmp
        result += str(coin[i]) + '원 동전 ' + str(tmp) + '개, '
    return result[:-2]
print(greedy())