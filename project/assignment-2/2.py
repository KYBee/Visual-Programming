print("종료 하시려면 종료를 입력해주세요")

while True:
    sentence = input("문장을 입력하세요 : ")

    if sentence == "종료":
        break

    #입력된 문장 중 첫 번째 문장을 반환
    sentence = sentence.split(".")[0]
    sentence = sentence.split(" ")

    if sentence[0] == "저는":
        name = sentence[1]
        if name[-3:] == "입니다":
            print(name[:-3])
        elif name[-3:] == "이라고":
            if sentence[2] == "합니다":
                print(name[:-3])
            else:
                print("첫 문장이 잘못되었습니다. 다시 입력해 주세요.")
        else:   
            print("첫 문장이 잘못되었습니다. 다시 입력해 주세요.")
    elif sentence[0] == "제" and sentence[1] == "이름은":
        name = sentence[2]
        if name[-3:] == "입니다":
            print(name[:-3])
        else:
            print("첫 문장이 잘못되었습니다. 다시 입력해 주세요.")
    else:
        print("첫 문장이 잘못되었습니다. 다시 입력해 주세요.")
