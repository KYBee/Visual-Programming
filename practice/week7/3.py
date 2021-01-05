operators = "+-*"
numbers = []
operator = []
print("종료하려면 종료를 입력하세요")

while True:

    sentence = input("수식을 입력하세요: ")

    if sentence == "종료":
        break

    temp = ""
    numbers = []
    operator = []
    result = 0

    for character in sentence:
        if character in operators:
            operator.append(character)
            numbers.append(temp)
            temp = ""
        else:
            temp += character


    i = 0
    while len(operator) > 0:
        for op in range(len(operator):
            if operator[op] == "*":
                result += numbers[i] * numbers[i + 1]
                numbers[i] = result
                del numbers[i + 1]
                del operator[i]
                i -= 1

        i += 1


            
