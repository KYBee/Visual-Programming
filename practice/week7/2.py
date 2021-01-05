sentence = input("문장을 입력하세요").split()

print(sentence)
sentence_after = []

for i in range(len(sentence)):
    print(sentence[i])
    compare = sentence[:i] + sentence[i + 1:]
    if sentence[i] not in compare:
        sentence_after.append(sentence[i])

print(sentence_after)
result = ", ".join(sentence_after)

print(result)
