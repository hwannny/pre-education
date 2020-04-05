'''
4.
다중상속을 이용하여 카드사의 클래스를 만들고
영화카드는 20% 할인
마트카드는 10% 할인
교통은 10%할인을 받는 카드 class를 구현하시오


테스트코드
<입력>
multi_card=Multi_card()
multi_card.charge(20000)
multi_card.consume(5000,'마트')
multi_card.consume(10000,'영화관')
multi_card.consume(2000,'교통')
multi_card.print()

<출력>
카드가 발급 되었습니다.
20000이 충전되었습니다.
마트에서 4500.0원을 사용했습니다.
영화관에서 8000.0원을 사용했습니다.
교통에서 1800.0원을 사용했습니다.
잔액이 5700.0원 입니다
'''


class Movie_card:
    dc = 20


class Mart_card:
    dc = 10


class Traffic_card:
    dc = 10


class Multi_card(Movie_card, Mart_card, Traffic_card):
    def __init__(self):
        print('카드가 발급되었습니다.')
        self.martDC = (100 - Mart_card.dc) / 100
        self.movieDC = (100 - Movie_card.dc) / 100
        self.trafficDC = (100 - Traffic_card.dc) / 100

    def print(self):
        print('잔액이 {}원 입니다.'.format(self.money))

    def charge(self, money):
        self.money = money
        print('{}이 충전되었습니다.'.format(money))

    def consume(self, payMoney, place):
        if self.money < payMoney:
            print('잔액이 부족합니다.')

        elif place == '마트':
            dcPayMoney = payMoney * self.martDC
            self.money = self.money - dcPayMoney
            print('{}에서 {}원 사용했습니다.'.format(place, dcPayMoney))

        elif place == '영화관':
            dcPayMoney = payMoney * self.movieDC
            self.money = self.money - dcPayMoney
            print('{}에서 {}원 사용했습니다.'.format(place, dcPayMoney))

        elif place == '교통':
            dcPayMoney = payMoney * self.trafficDC
            self.money = self.money - dcPayMoney
            print('{}에서 {}원 사용했습니다.'.format(place, dcPayMoney))

        else:
            self.money = self.money - payMoney
            print('{}에서 {}원 사용했습니다.'.format(place, payMoney))


multi_card = Multi_card()
multi_card.charge(20000)
multi_card.consume(5000, '마트')
multi_card.consume(10000, '영화관')
multi_card.consume(2000, '교통')
multi_card.print()
