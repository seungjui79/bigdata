# 현재 파이썬의 working directory 확인
print(os.getcwd())

# CWD가 다르므로 절대경로로 path 지정
path = 'C:\Users\이승주\Desktop\bigdata\File I_O.py'
fp = open(path)
str = fp.read()
print(str, end='')
fp.close()