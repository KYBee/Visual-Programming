weather_list = list()
city_list = list()

def average_temperature(weather):
    cnt = 0
    last = weather[0][2][:7]
    temp_sum = 0
    temp_dir = list()
    temp_average = 0

    for i in weather:
        if last != i[2][:7]:
            temp_average = round(temp_sum / cnt, 1)
            temp_dir.append([last, temp_average])
            last = i[2][:7]
            cnt = 1

            if i[3] == "":
                if i[4] != "" and i[5] != "":
                    temp_sum = (float(i[4]) + float(i[5])) / 2
                elif i[4] == "" and i[5] == "":
                    temp_sum = 0
                else:
                    if i[4] == "":
                        temp_sum = float(i[5])
                    else:
                        temp_sum = float(i[4])
            else:
                temp_sum = float(i[3])

        else:
            if i[3] == "":
                if i[4] != "" and i[5] != "":
                    temp_sum += (float(i[4]) + float(i[5])) / 2
                elif i[4] == "" and i[5] == "":
                    temp_sum += 0
                else:
                    if i[4] == "":
                        temp_sum += float(i[5])
                    else:
                        temp_sum += float(i[4])
            else:
                temp_sum += float(i[3])

            cnt += 1
    #마지막 달 추가
    temp_dir.append([last, round(temp_sum/cnt, 1)])
    return temp_dir

def monthly_rain(weather):
    rain_sum = 0
    last = weather[0][2][:7]
    rain_dir = list()
    
    for i in weather:
        if last != i[2][:7]:
            rain_dir.append([last, round(rain_sum, 1)])
            last = i[2][:7]
            if i[6] == "":
                rain_sum = 0
            else:
                rain_sum = float(i[6])
        else:
            if i[6] == "":
                rain_sum = 0
            else:
                rain_sum += float(i[6])
    #마지막 달 추가
    rain_dir.append([last, round(rain_sum, 1)])
    return rain_dir

with open("weather.csv", "r") as f:
    #맨 윗 줄 제거
    line = f.readline().strip()
    while True:
        line = f.readline()
        if not line:
            break

        line = line.strip()
        line = line.split(",")
        weather_list.append(line)
        
        if line[1] not in city_list:
            city_list.append(line[1])

city_weather_list = list()
print("도시를 선택하세요 (", end="")
cnt = 0
for i in city_list:
    print("%d:%s " % (cnt + 1, city_list[cnt]), end="")
    cnt += 1
option = int(input(") ")) - 1

print(city_list[option])
print("기후 분석\t\t평균 기온\t월별 강수량(mm)")

for i in weather_list:
    if i[1] == city_list[option]:
        city_weather_list.append(i)

city_temperature_average = average_temperature(city_weather_list)
city_precipitation = monthly_rain(city_weather_list)

for i in range(len(city_temperature_average)):
    print("  %s\t\t   %.1f\t\t   %.1f" % (city_temperature_average[i][0], city_temperature_average[i][1], city_precipitation[i][1]))
