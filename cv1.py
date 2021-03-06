import cv2

#이미지 불러오기
이미지 = cv2.imread("flowers.jpg")

#크기변경
크기변경 = cv2.resize(이미지, (500, 500))

# 글자넣기 - 10, 30 = 위치, TEXT- 폰트와 폰트크기,   255,0,255=폰트색상 , 진하게
cv2.putText(크기변경, "Hello songju!", (10, 30), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 255), 3)
# 빨강색 : (0, 0, 255)
# 주황색 : (0, 187, 255)
# 노랑색 : (0, 228, 255)
# 초록색 : (0, 255, 0)
# 파란색 : (255, 0, 0)
# 핑크색 : (255, 0, 255)
# 보라색 : (255, 0, 95)
# 흰색 : (255, 255, 255)
# 검은색 : (0, 0, 0)

# 이미지 보여주기(제목, 이미지명)
cv2.imshow("title", 크기변경)

#이미지 띄워놓고 대기
cv2.waitKey(0)