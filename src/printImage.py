# python에서 Opencv를 사용하기 위해
import cv2

# 파일이 저장된 경로
imageFile = "../data/lena.jpg"

# cv2 모듈을 이용해서 imageFile에 저장된 이미지 경로에서 imread( image read )를 하고 img에 해당 바이트 코드를 넣어준다.
img = cv2.imread(imageFile )        # cv2.IMREAD_COLOR
# print( type( img ) )        # [result] <class 'numpy.ndarray'>

# cv2 모듈을 이용해서 imageFile 경로의 사진을 GRAYSCALE로 읽어들인다.
imgGray = cv2.imread( imageFile, cv2.IMREAD_GRAYSCALE )
# print( type( img ) )        # [result] <class 'numpy.ndarray'>

# Lena color image 라는 이름으로 Window가 생성된다.
cv2.imshow('Lena color image', img )

# Lena grayscale image 라는 이름으로 Window가 생성된다.
cv2.imshow('Lena grayscale', imgGray )


# 키보드 입력 대기 - 키를 누르면 모든 창이 닫힌다.
cv2.waitKey()
cv2.destroyAllWindows()
