sentence = input("문장을 입력하세요: ").split()


while True:
    change_word = input("검색할 단어 변경할 단어?: ")
    
    if change_word == "end":
        break
    else:
        change_word = change_word.split()
        if len(change_word) < 2:
            print("단어를 한개만 입력하셨습니다.")
            print("검색할 단어와 변경할 단어 두 개 입력해주세요")
            continue

    if change_word[0] not in sentence:
        print("입력하신 단어는 존재하지 않습니다.")
    else:
        for i in range(len(sentence)):
            if sentence[i] == change_word[0]:
                sentence[i] = change_word[1]
                break
            
    print(" ".join(sentence))
