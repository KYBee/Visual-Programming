import writemodule
import readmodule

print("csv 파일만 사용 가능하며, 확장자는 입력하실 필요 없습니다.")
lines, f_name = readmodule.readdata()
data = list()

for line in lines:
    line = line.strip().split(",")
    data.append(line)

readmodule.showtable(data)
final_data = writemodule.makerank(data)
readmodule.showtable(final_data)

writemodule.makereport(final_data, f_name)
