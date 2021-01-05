def str_to_int(int_numbers):
    int_num = []
    for str_num in int_numbers:
        int_num.append(int(str_num))

    return int_num

def print_number_array(arr_print):
    for num in arr_print:
        print(" %3d" % num, end= " ")
    print()

def print_char_array(arr_print):
    for num in arr_print:
        print(" %3s" % num, end= " ")
    print()

def add_array(numbers, add_numbers):
    for i in range(len(numbers)):
        add_numbers[i] += numbers[i]

    return add_numbers

def count_differ(yesterday, now):
    for i in range(len(yesterday)):
        now[i] -= yesterday[i]
        if now[i] > 0:
            now[i] = "+" + str(now[i])
        else:
            now[i] = str(now[i])

    return now

change = [0] * 17
total = [0] * 17
trial = 0

while True:
    today = input("%d일차 : " % (trial + 1)).split(",")
    if today[0] == "종료":
        break

    today = str_to_int(today)
    change = count_differ(change, today.copy())
    total = add_array(today, total)

    print("     서울 부산 대구 인천 광주 대전 울산 세종 경기 강원 충북 충남 전북 전남 경북 경남 제주 ")
    print("오늘", end="")
    print_number_array(today)
    print("변동", end="")
    print_char_array(change)
    print("누계", end="")
    print_number_array(total)

    change = today
    trial += 1

    print()
