a = int(input("숫자를 하나 입력하세요: "))
print(bin(a))


while a > 0:
    print(a & 1, end = "")
    a = a >> 1
