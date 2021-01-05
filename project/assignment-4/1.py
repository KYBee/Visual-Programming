word_dict = dict()

with open("dict_test.TXT", "r") as f:

    while True:
        line = f.readline()

        if not line:
            break

        line = line.strip()
        line = line.split(" : ")

        #단어 혹은 뜻만 있는 사전의 단어 제거
        if len(line) == 2:
            word_dict[line[0]] = line[-1]

print("종료를 원하시면 -1를 입력하세요")
while True:
    english = input("단어? ")
    if english == "-1":
        break
    elif english not in word_dict:
        print("목록에 없는 단어 입니다.")
    else:
        print(english, word_dict[english])
