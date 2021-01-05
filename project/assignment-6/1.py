import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import xlrd

title = "20th election"


while True :
    # 100회 반복

    wb = xlrd.open_workbook(filename = "elec.xlsx")
    ws = wb.sheet_by_name("Sheet1")

    data = []

    for r in range(ws.nrows):
        col = []
        for c in range(ws.ncols):
            col.append(ws.cell(r, c).value)
        data.append(col)

    values = data[1]

    labels = data[0]
    for i in range(len(labels)):
        labels[i] = str(i + 1) + "번 " + labels[i] 

    plt.rc('font', family="nanumGothic")
    plt.title(title)
    plt.pie(values, explode=(0.1, 0.1, 0.1, 0.1, 0.1), labels=labels,
    autopct='%1.1f%%', startangle=67)
    plt.draw()
    # 그리기
    plt.pause(10) # 10초 기다리기
    plt.clf() # figure 지우기