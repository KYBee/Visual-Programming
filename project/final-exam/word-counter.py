import sys

# word_lower은 두가지 기능이 있는 함수이다.
# 1. 문자의 대문자를 소문자로 바꾸어 주는 기능
# 2. 문자의 , . 등을 제거하는 기능
# 1번은 대소문자를 동일한 조건에서 비교하기 위해 소문자로 통일시키기 위함이며
# 2번은 현 파일에는 포함되지 않았지만 .의 사용으로 만약 end. 와 같은 파일이 들어올 경우 end로 counting을 시켜주기 위함이다.
def word_lower(w):
    output = ""
    for ch in w:
        if ch.isalpha():
            output += ch
    return output.lower()

# 파일이름을 입력받아서 해당 파일이 존재하면 데이터를 읽고 존재하지 않는다면 프로그램을 종료한다.
try:
    fname = input("파일 이름: ")
    file = open(fname, "r")
except:
    print("No File existed. Check Again")
    sys.exit()
else:
    # 파일이 존재한다면 내부의 데이터를 단어별로 split한 뒤에 소문자로 바꾼다.
    table = dict()
    for line in file:
        words = line.split()
        for word in words:
            # 단어를 모두 소문자로 바꾸는 코드
            word = word_lower(word)
            # 단어가 이미 table에 존재해서 counting이 되고 있다면 1을 추가해준다.
            # 단어가 이전에 입력되지 않았던 새로운 단어라면 새로 dictionary의 key 값으로 추가해준다. 이때 value 값은 1이다.
            if word not in table:
                table[word] = 1
            else:
                table[word] += 1
    file.close() 

# 파일에서 추출한 단어들은 현재 dictionary 형태로 저장되어 있다.
# 이를 list 형식으로 변환 후 sorting 한 후에 10개를 뽑아낸다.
table = list(table.items())
table.sort(key = lambda x: x[1], reverse = True)
table = table[:10]



# 사전을 담을 dictionary 이다.
word_dict = dict()
with open("dict_test.TXT", "r") as f:
    # 사전의 처음부터 끝까지 한 문장씩 읽어온다. 끝까지 읽은 뒤에 while 루프를 탈출하고 파일을 닫는다.
    while True:
        line = f.readline()

        if not line:
            break

        line = line.strip()
        line = line.split(" : ")

        # 단어 혹은 뜻만 있는 사전의 단어 제거한다.
        if len(line) == 2:
            word_dict[line[0]] = line[-1]

# 현재 사전의 내용은 word_dict, 단어 counting 결과는 table에 들어있다.
for word in table:
    try:
        print(word[0], "(%d) : " % word[1], word_dict[word[0]], sep="")
    except:
        print(word[0], "(%d) : " % word[1], sep="")
