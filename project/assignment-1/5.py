
#코드 1

import time
import math

#0과 1은 소수가 아님
prime_num = [False, False]
prime_count = 0

start = time.time()

#인덱스 2부터 100000까지 일단 True 값을 넣어서 소수로 추정
for i in range(2, 100001):
    prime_num.append(True)

#배수들을 False로 바꿈
for i in range(2, 100001):
    if prime_num[i] == True:
        for j in range(i + i, 100001, i):
            prime_num[j] = False

#True 값들의 숫자를 셈
for i in range(2, 100001):
    if prime_num[i] == True:
        prime_count += 1

print(prime_count, '개')
print("코드 실행 시간: %.2f초" % (time.time() - start))


"""
#코드 2

import time

prime_num = []

start = time.time()

for i in range(2, 100000):
    prime_flag = 1

    for j in prime_num:
        if i % j == 0:
            prime_flag = 0
            break
            
    if prime_flag == 1:
        prime_num.append(i)

print(len(prime_num), '개')
print("코드 실행 시간: %.2f초" % (time.time() - start))

"""
