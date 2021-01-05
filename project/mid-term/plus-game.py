from random import randint
from time import time
import math

operators = "*+"
trying = 3
total_score = 0

while trying > 0:
    numbers = []
    op = []

    numbers.append(randint(2, 9))

    #range의 숫자를 변경하면 숫자 2개가 아닌 여러개의 덧셈과 곱셈도 가능
    #물론 2개의 숫자 말고 여러개의 숫자를 받을 경우에는
    #계산의 순서를 제어하는 함수도 필요하지만 해당 문제에서는 구현 안함
    for i in range(1):
        op.append(operators[randint(0, 1)])
        numbers.append(randint(2, 9))


    print(numbers[0], end=" ")
    for i in range(len(op)):
        print("%s %d " % (op[i], numbers[i + 1]), end="")

    start_time = time()
    answer = int(input("= "))
    time_spend = time() - start_time

    score = round(2 - time_spend, 1)

    if score < 0:
        trying -= 1
        print("시간 초과입니다. (기회 %d)" % trying)
        continue


    for character in range(len(op)):
        if op[character] == "+":
            numbers[character + 1] = numbers[character] + numbers[character + 1]
        else:
            numbers[character + 1] = numbers[character] * numbers[character + 1]

    if answer == numbers[len(op)]:
        score = 100 * score
        total_score += score
        print("%d점 획득. 총점 %d점(기회 %d번)" % (score, total_score, trying))
    else:
        trying -= 1
        print("틀렸습니다. 총점 %d점(기회 %d번)" % (total_score, trying))

print("총 %d점을 기록하셨습니다." % total_score)

