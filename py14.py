a = 7
b = 2
print("{}+{}={}".format(a, b, a+b))           # 더하기
print("{}-{}={}".format(a, b, a-b))           # 빼기
print("{}*{}={}".format(a, b, a*b))           # 곱하기
print("{}**{}={}".format(a, b, a**b))         # 제곱승
print("{}/{}={}".format(a, b, a/b))           # 나누기(소수점까지)
print("{}//{}={}".format(a, b, a//b))         # 나누기(소수점 땜)
print("{}%{}={}".format(a, b, a%b))           # 나머지 구하기    ,p73

'''   85p
10~99 사이의 정수를 입력하세요 >>> 45
십의자리 : 4
일의자리 : 5
'''
# 힌트 : 10으로 나누면 십의자리, 10으로 나눈 나머지는 일의자리
정수 = int(input("10 ~ 99 사이의 정수를 입력하세요>>>"))
변수 = 정수%10
print("십의자리 :{}".format(정수//10))
print("일의자리 :{}".format(변수))
