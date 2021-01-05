def makerank(table):
    columns = table[0]
    table = table[1:]
    col_count = len(columns)
    error = 0
    s_index = 0
    end_index = len(table)

    #예외 처리 및 총점 구하기
    while s_index < end_index:
        total = 0

        #이름 부분이 비어있는 경우
        if table[s_index][0] == "":
            print("잘못된 데이터가 존재합니다.", table[s_index])
            del table[s_index]
            end_index -= 1
            continue

        #더 많은 수 혹은 적은 수의 데이터가 제공된 경우
        if len(table[s_index]) != col_count:
            print("잘못된 데이터가 존재합니다.", table[s_index])
            del table[s_index]
            end_index -= 1
            continue


        for j in range(1, col_count):
            try:
                temp = table[s_index][j]
            except:
                error = 1
                print("잘못된 데이터가 존재합니다.", table[s_index])
            else:
                #빈 데이터가 있을 경우
                try:
                    total += int(table[s_index][j])
                except:
                    print("잘못된 데이터가 존재합니다.", table[s_index])
                    error = 1
                else:
                    #음수가 있을 경우
                    if int(table[s_index][j]) < 0:
                        print("잘못된 데이터가 존재합니다.", table[s_index])
                        error = 1
        if error == 1:
            error = 0
            del table[s_index]
            end_index -= 1
        else:
            table[s_index].append(str(total))
            s_index += 1


    # 석차 구하기
    score_sum = list()
    for i in table:
        score_sum.append(i[col_count])

    score_sum.sort()
    for i in table:
        i.append(str(score_sum.index(i[col_count]) + 1))
    
    return [columns + ['총점', '석차']] + table



def makereport(table, f_name):
    report_name = f_name + "_report.txt"

    while True:
        try:
            report = open(report_name, 'r', encoding="utf-8")
        except IOError:
            exist = 0
        else:
            exist = 1
            #일단 먼저 닫아주고
            report.close()
            while True:
                override = input("파일이 이미 존재합니다. 해당 파일을 덮어쓰시겠습니까? (yes or no) ")
                if override == "yes":
                    override = 1
                    break
                elif override == "no":
                    report_name = input("다른 이름을 입력해 주세요. ") + "_report.txt"
                    override = 0
                    break
                else:
                    print("yes 와 no로 대답을 입력해 주세요.")
        
        if exist == 0 or override == 1:
            break

    with open(report_name, "w", encoding="utf-8") as report:
        for i in table:
            report.write(','.join(i) + "\n")


