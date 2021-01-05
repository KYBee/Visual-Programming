from random import randint 

def lotto_generator():
    lotto_num = []

    while len(lotto_num) < 6:
        random_number = randint(1, 45)
        if random_number not in lotto_num:
            lotto_num.append(random_number)

    return lotto_num

def print_number_array(numbers):
    for num in numbers:
        print("%2d" % num, end= " ")
    
    print()

while True:
    count = int(input("원하는 숫자를 선택하세요. (1 ~ 100) "))

    if count >= 1 and count <= 100:
        break
    else:
        print("1~100 사이의 수를 입력하세요")
    
trial = 0

while trial < count:
    lotto = lotto_generator()
    #로또 번호를 sorting 했음
    lotto.sort()

    print("%3d회 :" % (trial + 1), end=" ")
    print_number_array(lotto)

    trial += 1

print("\n이주의 로또 번호: ")
print_number_array(lotto)

