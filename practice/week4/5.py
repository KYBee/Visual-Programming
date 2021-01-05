word_list = []

for i in range(5):
    typed_word = input("")
    word_list.append(typed_word)

word_list.sort()
print("목록 :", word_list)
print("중앙의 단어 :", word_list[2])
