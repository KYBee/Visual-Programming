import random
import numpy as np
import matplotlib.pyplot as plt
from functools import reduce

list1 = []
list2 = []

for i in range(1000):
    list1.append(random.randint(0, 100))
    #np.random.normal(50, 20, 1000) 을 이용하여 1000개를 한번에 뽑을 수 있지만
    #범위를 0~100으로 지정하기 위해서 적당한 mean과 stdev를 넣고 한 개씩 뽑도록 했습니다.
    while True:
        temp = np.random.normal(50, 20)
        temp = int(temp)
        if temp >= 0 and temp <= 100:
            list2.append(temp // 1)
            break

#히스토그램
title = "Data"
plt.title(title)
plt.hist(list1, bins=20, density=True, alpha=0.7, histtype="stepfilled")
plt.hist(list2, bins=20, density=True, alpha=0.7, histtype="stepfilled")
plt.legend(['random.randint', 'np.random.normal'])

plt.show()