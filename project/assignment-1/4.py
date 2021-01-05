print("데이터를 입력하세요(입력을 마치려면 0을 입력하세요)")
data_list = []


while True:
    data = int(input(""))
    
    if data == 0:
        break
    else:
        data_list.append(data)

data_list.sort()

print("결과 : ", end = "")
for num in data_list:
    print(num, end = " ")
print("(%d개)" % len(data_list))
