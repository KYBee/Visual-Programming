from random import randint

print("가위바위보 게임")
decision = ('가위', '바위', '보')
computer_win = 0 #컴퓨터의 승리 == 나의 패배
user_win = 0 #나의 승리 == 컴퓨터의 패배
round = 1

while computer_win < 3 and user_win < 3:
    print()  #보기 좋게 하기 위한 줄 바꿈
    print("컴퓨터 : %d승 %d패,  당신 : %d승 %d패" % (computer_win, user_win, user_win, computer_win))
    print("(라운드 %d)" % round)

    computer_decision = decision[randint(0, 2)]
    print("컴퓨터가 결정했습니다.")
    user_decision = input("무엇을 내시겠습니까? (가위, 바위, 보) ")
    if user_decision not in decision:
        print('가위, 바위, 보 중에서 내셔야 합니다.')
        continue

    if computer_decision == user_decision:
        print("컴퓨터는 %s, 당신은 %s, 비겼습니다." % (computer_decision, user_decision))
    elif computer_decision == '가위':
        if user_decision == '보':
            print("컴퓨터는 %s, 당신은 %s, 컴퓨터가 이겼습니다." % (computer_decision, user_decision))
            computer_win += 1
        else:
            print("컴퓨터는 %s, 당신은 %s, 당신이 이겼습니다." % (computer_decision, user_decision))
            user_win += 1
    elif computer_decision == '바위':
        if user_decision == '가위':
            print("컴퓨터는 %s, 당신은 %s, 컴퓨터가 이겼습니다." % (computer_decision, user_decision))
            computer_win += 1
        else:
            print("컴퓨터는 %s, 당신은 %s, 당신이 이겼습니다." % (computer_decision, user_decision))
            user_win += 1
    else:
        if user_decision == '바위':
            print("컴퓨터는 %s, 당신은 %s, 컴퓨터가 이겼습니다." % (computer_decision, user_decision))
            computer_win += 1
        else:
            print("컴퓨터는 %s, 당신은 %s, 당신이 이겼습니다." % (computer_decision, user_decision))
            user_win += 1
    round += 1


print()
print("총 %d라운드를 진행했습니다. 최종 스코어는 아래에 표시됩니다." % round)
print("컴퓨터 : %d승 %d패,  당신 : %d승 %d패" % (computer_win, user_win, user_win, computer_win))
