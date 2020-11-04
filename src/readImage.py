import cv2

imageFile = "../data/lena.jpg"

img = cv2.imread( imageFile )

cv2.imwrite("test_lena.bmp", img )

cv2.imwrite("test_lena.png", img)

# 0~9 사이의 숫자로 압축률을 정한다. default로는 3이다.
cv2.imwrite("test_comp_lena.png", img, [cv2.IMWRITE_PNG_COMPRESSION, 9] )

# jpg의 품질을 90%로 설정한다. default는 95%이다.
cv2.imwrite("test_quality_lena.jpg", img, [cv2.IMWRITE_JPEG_QUALITY, 90] )