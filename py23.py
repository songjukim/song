# 차량 2부제 실시, 짝수로 끝나면 운행가능, 홀수로 끝나면 운행불가
# 차량번호를 입력하세요>>>237가1234
# 차량번호 237가1234는 오늘 운행가능 입니다.
# 99페이지

number = int(input("차량번호를 입력하세요>>>"))
if int(number[-2]) % 2 == 0:
    print("차량번호 {}는 오늘 운행가능 입니다".format(number))
if int(number[-2]) % 2 == 1:
    print("차량번호 {}는 오늘 운행불가 입니다".format(number))