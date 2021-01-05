print("전화번호 추가를 원하시면 'add'를 입력하시고\n종료를 원하시면 '-1'을 입력해주세요")

phone_numbers = {'홍길동': '010-4444-5555', '김중앙':'010-9191-8181', '심청': '010-3232-5454'}

while True:
    phone_numbers_list = list(phone_numbers.keys())
    input_list = []

    name = input("이름>> ")
    if name == '-1':
        break
    elif name == 'add':

        while True:
            name_add = input("이름은? ")
            if name_add not in phone_numbers_list:
                break
            else: 
                print("동일한 이름이 있습니다. 다시 입력해 주세요")

        phone_add = input("전화번호는? ")
        phone_numbers[name_add] = phone_add
        print("%s 전화번호가 추가되었습니다." % name_add)
        continue

    for temp_name in phone_numbers_list:
        if name in temp_name:
            input_list.append(temp_name)

    if len(input_list) == 0:
        print("찾을 수 없습니다.")
    else:
        for name in input_list:
            print("%s  %s" % (name, phone_numbers[name]))



