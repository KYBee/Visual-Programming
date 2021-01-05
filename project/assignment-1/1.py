# num 입력받는 숫자
# abs_num 절댓값


while True:
    num = int(input(("숫자를 입력하세요 ")))

    if num == 0:
        break
    
    abs_num = num if num > 0 else -num
    print(abs_num)
