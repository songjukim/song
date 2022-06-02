학점 = int(input("점수를 입력하세요>>>"))
if 학점 >= 90:
    print("점수는 {}점이고, 학점은 A 학점 입니다".format(학점))
elif 학점 >= 80:
    print("점수는 {}점이고, 학점은 B 학점 입니다".format(학점))
elif 학점 >= 70:
    print("점수는 {}점이고, 학점은 C 학점 입니다".format(학점))
elif 학점 >= 60:
    print("점수는 {}점이고, 학점은 D 학점 입니다".format(학점))
elif 학점 >= 0:
    print("점수는 {}점이고, 학점은 F 학점 입니다".format(학점))