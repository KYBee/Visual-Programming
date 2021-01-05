import random

def print_cities(city, player, start, end, op):

    #op가 1인 경우 첫번째 줄, -1인 경우 2번째 줄
    if op == 1:
        arrow = "->"
    else:
        arrow = "<-"


    #위의 가로줄을 그림
    for i in range(start, end, op):
        print('%s' % "-" * 15, end=" " * 5)
    print()

    #도시의 번호와 이름을 출력함
    for i in range(start, end, op):
        print("|%-2s%-11s|" % (i + 1, city[i].name), end=" " * 5)
    print()

    #도시의 소유주를 출력함
    for i in range(start, end, op):
        print("|%8s %-4d|" % ("owner:", city[i].owner), end=" " * 5)
    print()

    #도시 밖의 화살표를 표시하기 위한 row
    for i in range(start, end, op):
        if (op == 1 and i != end - 1) or (op == -1 and i != end + 1):
            print("|%13s|" % " ", end=" " * 2 + arrow + " " * 1)
        else:
            print("|%13s|" % " ", end=" " * 5)
    print()

    #player의 위치를 표시하기 위한 row
    for i in range(start, end, op):
        print("|%4s" % " ", end="")            

        for j in range(len(player)):
            if i == player[j].location:
                print("%2s" % str(j + 1), end="")
            else:
                print("%2s" % " ", end="")
        print("%5s|" % " ", end=" " * 5)
    print()

    #아래 가로줄을 그린다.
    for i in range(start, end, op):
        print('%s' % "-" * 15, end=" " * 5)
    print()  
    

#마블 판을 출력하는 함수.
"""
game_status와 print_cities를 따로 선언한 이유는
마블 판의 2줄 중 윗줄은 1, 2, 3, 4, 5 순서이지만
아래 줄은 10, 9, 8, 7, 6 순서로 print해야 하므로 옵션을 다르게 주기 위함
만약 하나의 함수에 해당 기능을 구현했다면 코드가 너무 길어질 수 있음
"""
def game_status(city, player):
    #col_count는 한 행에 표시할 도시 수.
    #ex) 도시가 10개 있으면 한 행에 5개 도시 표시. 12개 도시가 있으면 한 행에 6개 도시 표시
    col_count = len(city) // 2
    row = 0

    while row < 2:
        city_cnt =  col_count

        if row == 0:
            #print_cities에 city와 player를 보내고, 0부터 4까지 1씩 증가하면서 print 하도록 요청
            print_cities(city, player, 0, city_cnt, 1)
        else:
            #print_cities에 city와 player를 보내고, 9부터 5까지 1씩 감소하면서 print 하도록 요청
            print_cities(city, player, len(city) - 1, city_cnt - 1, -1)

        print("\n")

        row += 1


#모든player들의 잔액을 출력해주는 함수
def player_balance(players, num=-1):
    if num == -1:
        for i in range(len(players)):
            print("%d번 플레이어의 잔액: %d" % (i + 1, players[i].balance))
    else:
        print("%d번 플레이어의 잔액: %d" % (num, players[num-1].balance))




class City:
    def __init__(self, name):
        self.name = name
        self.owner = 0

    def getOwner(self):
        return self.owner

    def setOwner(self, owner):
        self.owner = owner

    def IsEmpty(self):
        if self.owner==0:
            return True
        return False



class Player:
    def __init__(self):
        self.balance = 4000
        self.location = 0
        self.asset=[]

    #주사위를 굴리는 메소드. main 함수에서 코드를 간략하게 하기 위해
    def roll_dice(self):
        return random.randint(1, 6)

    def move(self,dice):
        self.location = (self.location + dice) % 10

    def buy_city(self):
        if self.balance >= 300:
            self.balance = self.balance - 300
            return True
        else:
            return False
            # 구매하는 것을 실패했다.

    #통행료 지불을 위한 메소드
    def pay_fee(self, target):
        self.balance -= 500
        target.balance += 500

#초기 setting
city = [City("Start"), City('Seoul'), City('Tokyo'), City('Sydney'), City('LA'), 
        City('Cairo'), City('Phuket'), City('NewDelhi'), City('Hanoi'), City('Paris')]
player=[Player(),Player()]


count = 1
end=0
#패배자를 찾기 위함
loser = 0

#게임 시작 전 마블 판을 한번 출력
print("Before Start: ")
game_status(city, player)

while count <= 30:
    print("=" * 100)
    print('%d번째 판' % count)
    count = count + 1

    for i in range(len(player)):
        main_player = player[i]
        dice = main_player.roll_dice()
        """
        리스트의 indexing과 player의 아이디가 다르기 때문에 지정한 변수
        컴퓨터는 player1을 player0으로 인지하지만, 우리는 player1로 사용하는 중
        해당 변수가 없어도 지정만 잘 해주면 프로그램은 동작함
        but 프로그램에 입력해줄 때와 화면으로 출력해줄 때 i, i+1 등으로 control 해야 하기 때문에 난잡해질 수 있음
        가독성을 위한 변수
        """
        player_id = i + 1

        print('%d 번 플레이어의 주사위가 %d이 나왔다'%(player_id, dice))
        main_player.move(dice)

        if city[main_player.location].name == "Start":
            print("출발점에 도착했습니다. 아무일도 일어나지 않습니다.")
            player_balance(player, player_id)
            print()
        elif city[main_player.location].IsEmpty():
            print('%s에 도착 (주인없음)' % city[main_player.location].name)

            if main_player.buy_city():
                city[main_player.location].owner = player_id
                #player의 이름을 owner로 설정
                print('%d번 플레이어는 %s를 구입한다.'%(player_id, city[main_player.location].name))
            else:
                print('잔고가 부족하여 구입할 수 없다.')
            player_balance(player, player_id)
            print()
        else:
            print('%s에 도착 (%i이 소유)' % (city[main_player.location].name, city[main_player.location].getOwner()))
            if city[main_player.location].owner == player_id:
            #city에 저장된 owner의 숫자가 i 라면 -> 현재 main_player이라면 과 같은 표현
                player_balance(player, player_id)
                print()
            else:
                if player[i].balance < 500:
                    print('%d번 플레이어는 돈을 지불할수 없다.' % (player_id))
                    print()
                    end=1
                    loser = i
                    break
                else:
                    city_owner = player[city[main_player.location].getOwner() - 1]
                    main_player.pay_fee(city_owner)
                    player_balance(player, player_id)
                    print()
    if end:
        break
    else:
        game_status(city, player)
        player_balance(player)
        print("\n\n")

print("<FINISH>")
game_status(city, player)
print("플레이어들의 최종 잔액")

player_balance(player)

result = []
total_balance = []
for i in player:
    total_balance.append(i.balance)

total_balance.sort(reverse=True)

for i in player:
    result.append(total_balance.index(i.balance))

for i in range(len(player)):
    print("플레이어 %d-> 순위: %d" % (i + 1, result[i] + 1))
