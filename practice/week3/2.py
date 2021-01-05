# 복리계산
# 금액 = 원금 * (1 + 이자율)기간

init_money = int(input("원금 = "))
interest = int(input("이율% = ")) / 100

for year in range(1, 4):
    result = init_money * (1 + interest) ** year
    print(year, "년차 = ", result, sep = "")