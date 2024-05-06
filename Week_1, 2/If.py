# 조건을 만족하면 실행
# 만족하지 않은 경우 실행하지 않음
#if와 else, elif 이용 시 여러 조건을 분기할 수 있음

import os
os.system('clear')

num = int(input("정수형 숫자를 입력하세요: "))
if num < 0:
    num = 0
    print('음수라서 0으로 설정')
elif num == 0:
    print('0 입니다.')
elif num == 1:
    print('1 입니다.')
else:
    print('1보다는 큽니다.')