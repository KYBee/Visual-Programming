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
last_word = "apple"
answer_list = []

while True:
    english = input("%s 끝말 잇기? " % last_word)
    if english == "-1":
        break
    elif english not in word_dict:
        print("사전에 없는 단어입니다(%s의 끝말을 이으세요)." % last_word)
    elif english in answer_list:
        print("중복된 단어입니다(%s의 끝말을 이으세요)." % last_word)
    elif len(english) > 5:
        print("단어가 길어요(%s의 끝말을 이으세요)." % last_word)
    elif len(english) < 5:
        print("단어가 짧아요(%s의 끝말을 이으세요)." % last_word)
    elif word_dict[english][0] != 'n' and word_dict[english][0] != 'N':
        print("사전에 없는 단어입니다(%s의 끝말을 이으세요)." % last_word)
    else:
        print("정답입니다(%s의 끝말을 이으세요)." % english)
        answer_list.append(english)
        last_word = english
