num_string = "영일이삼사오육칠팔구"
one_string = "일십백천"
man_string = "일만억"

print("숫자는 9억 이하로 입력해주시고 종료하시려면 음수를 입력하세요")

while True:
    number = input("숫자는? ")

    #9억 이하의 수만 입력받도록 했음. 음수 입력시 프로그램 종료
    if int(number) > 900000000:
        print("9억 이하의 수를 입력 바랍니다.")
        continue
    elif int(number) < 0:
        break

    #,를 넣어주기 위한 코드
    #3자리씩 슬라이싱 후 저장할 리스트
    number_comma = []
    number_str = number

    while True:
        temp_length = len(number_str)
        #남은 문자열의 길이가 3보다 크면 3개씩 슬라이싱해서 number_comma리스트에 저장
        if temp_length > 3:
            number_comma.insert(0, number_str[temp_length - 3: temp_length])
            number_str = number_str[:temp_length - 3]
        #남은 문자열의 길이가 3개 이하면 그 문자열을 그대로 number_comma리스트에 저장
        else:
            number_comma.insert(0, number_str)
            break
    
    #join메소드를 이용해서 ,로 number_comma 원소들을 연결하여 출력
    print(','.join(number_comma))


    #한글로 출력하기 위한 코드
    #man_string를 위한 변수 초기화
    num_length = len(number)
    man = (num_length - 1) // 4

    #10000을 일만으로 인식하지 않기 위한 예외처리
    one_flag = 0
    if num_length == 5 and int(number[0]) == 1:
        one_flag = 1

    #100000001을 일억일만으로 인식하지 않도록 man변수를 조절하는 예외처리
    zero_flag = 0
    

    for i in range(num_length):
        #몇 번째 숫자인지를 파악함
        num_length = len(number) - i

        #해당 번째 숫자가 몇인지를 받아옴
        num = int(number[i])

        #one_string를 위한 num_length
        num_length = (num_length - 1) % 4

        #숫자를 출력함
        if num != 0:
            if one_flag == 1:
                one_flag = 0     
                zero_flag += 1       
            elif num != 1:
                print(num_string[num], end="")
                if num_length != 0:
                    print(one_string[num_length], end="")
                zero_flag += 1
            else:
                print(one_string[num_length], end="")
                zero_flag += 1

        #억, 만, 일을 출력함
        if num_length == 0:
            if man != 0 and zero_flag != 0:
                print(man_string[man], end="")

            man -= 1
            zero_flag = 0

    print("")
