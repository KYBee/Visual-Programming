address_list = ['흑석동', '사당동', '상도동', '노량진동', '규동']

while True:
    new_address = input("동을 입력하세요.(종료 를 입력하면 프로그램 종료) ")

    if new_address == '종료':
        break
    elif new_address in address_list:
        target_index = address_list.index(new_address) + 1
        print("%d번째 동입니다." % (target_index))
    else:
        print("새로운 동명입니다. %d번째 동으로 등록합니다." % (len(address_list) + 1))
        address_list.append(new_address)
