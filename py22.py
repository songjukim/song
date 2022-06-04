# 임의의 정수 3개 입력. 큰수 구하기
# 99페이지
a = int(input("정수1 입력>>>"))
b = int(input("정수2 입력>>>"))
c = int(input("정수3 입력>>>"))
if a > b:
   if a > c:
       print("가장 큰 수는 {}입니다".format(a))
   else:
       print("가장 큰 수는 {}입니다".format(c))
else:
    if b > c:
        print("가장 큰 수는 {}입니다".format(b))
    else:
        print("가장 큰 수는 {}입니다".format(c))
