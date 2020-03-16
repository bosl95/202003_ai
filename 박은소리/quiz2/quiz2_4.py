class movie():
    def movie(self, n):
        return n*0.8

class market():
    def market(self, n):
        return n*0.9

class traffic():
    def traffic(self, n):
        return n*0.9

class Multi_card(movie, market, traffic):
    def __init__(self):
        print('카드가 발급되었습니다.')
        self.money = 0

    def charge(self, n):
        self.money += n
        print('{}이 충전되었습니다.'.format(n))

    def consume(self, n, m):
        if m=='영화관': n = self.movie(n)
        elif m =='마트' : n = self.market(n)
        elif m =='교통' : n = self.traffic(n)

        self.money -= n
        print('{}에서 {}원을 사용했습니다.'.format(m, n))

    def print(self):
        print('잔액이 {}원입니다.'.format(self.money))

multi_card=Multi_card()
multi_card.charge(20000)
multi_card.consume(5000,'마트')
multi_card.consume(10000,'영화관')
multi_card.consume(2000,'교통')
multi_card.print()