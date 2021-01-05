def readdata():
    while True:
        f_name = input("이름은? ")

        error = 0

        try:
            f = open(f_name + ".csv", "r", encoding="utf-8")
        except IOError:
            print("파일이 존재하지 않습니다. 이름을 정확히 입력해 주세요.")
            error = 1

        if error != 1:
            break

    lines = f.readlines()
    f.close()

    return lines, f_name

#임의로 만든 함수
def showtable(table):
    print("전체 데이터")

    for record in table:
        for attribute in record:
            print("%10s " % attribute, end="")
        print()
