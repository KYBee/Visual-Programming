# 복리계산 => 금액 = 원금 * (1 + 이자율) ** 기간

init_money = int(input("원금을 입력하세요(원). "))
interest = int(input("금리를 입력하세요(%). ")) / 100
print("원금 %d원  금리 %d%% 입니다." % (init_money, interest * 100))
print("기간     합계")

for year in range(1, 21):
    result = init_money * (1 + interest) ** year
    print("%d년     %.2f" % (year, result))
