print("종료하시려면 종료를 입력하세요.")

while True:
    number = ""
    operator = "+-"
    number_list = []
    operator_list = []

    equation = input("수식을 입력하세요: ")

    if equation == "종료":
        break

    for op in equation:
        if op in operator:
            operator_list.append(op)
            number_list.append(int(number))
            number = ""
        else:
            number += op

    #마지막 숫자를 number_list에 더해줌
    number_list.append(int(number))

    result = number_list[0]

    for i in range(len(operator_list)):
        if operator_list[i] == '+':
            result += number_list[1 + i]
        else:
            result -= number_list[1 + i]

    print("결과는", result)

