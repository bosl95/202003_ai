class Card:
    money = 0
    def charge(self, n):
        self.money += n
        self.print()

    def consume(self, n, m):
        if m=='영화관': n = int(n*0.8)
        if self.money < n :
            print('잔액이 부족합니다.')
            return
        else:
            self.money -= n
            print('{}에서 {}원 사용했습니다.'.format(m, n))

    def print(self):
        print('잔액이 {}입니다'.format(self.money))
card = Card()
card.charge(20000)
card.consume(3000,'마트')
card.consume(10000,'영화관')
card.consume(13000,'마트')
card.print()