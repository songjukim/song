# 3의배수 판별 
# 989페이지

정수 = int(input("정수를 입력하세요>>>"))
if 정수%3 == 0:
    print("{}는 3의 배수 입니다".format(정수))
else:
    print("{}는 3의 배수가 아닙니다".format(정수))