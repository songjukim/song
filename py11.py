# 출력 (화면에 보여주기)
from tokenize import Name


print("안녕하세요")

# 변수 (저장공간)
# 변수 생성
변수이름 = "반갑습니다"

# 변수사용
print(변수이름)
print("안녕하세요", 변수이름)
print("안녕하세요 {}".format(변수이름))

# 입력 input
# 변수 = input("안내할 내용")
변수이름 = input("입력하세요>>>")
# 입력한 값을 출력
print(변수이름)

# 사칙연산
숫자1 = 100
숫자2 = 50
더하기 = 숫자1 + 숫자2
빼기 = 숫자1 - 숫자2
곱하기 = 숫자1 * 숫자2
나누기 = 숫자1 / 숫자2
print(더하기)
print(빼기)
print(곱하기)
print(나누기)

