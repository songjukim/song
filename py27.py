# for 변수명 in range(10):

# while
import time
'''
기준점 = 0
while 기준점<10:            # 원하는 횟수 만큼 출력
    time.sleep(1)          # 1초동안 멈춤
    print("10은 5보다 큽니다.")
    기준점 += 1
print("프로그램 종료")


while 조건:
    조건이 맞을때마다 실행할 코드

예제1) 10번출력하기
num=1
while num < 11:
    print(num,"번 했습니다")
    num +=1
'''
num=1
while num < 11:
    print(num,"번 했습니다")
    num +=1

n = 10
while n >= 1:
    print(n)
    n -= 1
'''
111페이지
숫자 1개를 입력받고, 그 숫자만큼 Hello 입력하기
'''
n = 1
정수 = int(input("정수를 입력하세요>>>"))
if 정수 <= 0:
    print("잘못된 입력입니다") 
else:
    while n <= 정수:
        print(n, "번째 Hello")
        n += 1
    
'''
111페이지
0~100까지 숫자중에서
7의 배수만 출력하기 (반복문 사용)
'''
num=1
while num <= 100:
    if num % 7 == 0:
        print(num)
    num = num + 1

flag = 1 
while flag < 101:
    if flag % 7 == 0:
        print(flag)
    flag = flag +1
   
'''
110페이지
구구단 2단부터 9단까지 출력
'''
dan=2
while dan <=9:
    n=1
    while n <= 9:
        print("{}*{}={}".format(dan, n, dan *n))
        n += 1
    dan += 1

       

    