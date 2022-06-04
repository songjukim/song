import cv2
# pip install opencv-python ㅡ...터미널에 입력하기
print("pip install opencv-python 완료!")


import cv2
# 이미지 불러오기
이미지 = cv2.imread("flowers.jpg")

# 이미지 보여주기 (제목, 이미지명)
cv2.imshou("title", 이미지)

# 이미지 띄워놓고 대기
cv2.waitkey(0)