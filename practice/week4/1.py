# C = 5/9(F - 32)

temp = float(input("온도? "))

cel_temp = round(5/9 * (temp - 32), 1)
fa_temp = round(9/5 * (temp) + 32, 1)

print("화씨 ", temp, "도는 섭씨 ", cel_temp, "도", sep = "")
print("섭씨 ", temp, "도는 화씨 ", fa_temp, "도", sep = "")
