import cv2
import os
from matplotlib import pyplot as plt

imageFile = "../data/lena.jpg"

# File이 존재하는지 확인하는 코드
if os.path.isfile( imageFile ) == False:
    print("no File : {}".format( imageFile ) )
else:
    # GrayScale로 이미지를 읽어온다. ( 8 비트 데이터? )
    imgGRAY = cv2.imread( imageFile, cv2.IMREAD_GRAYSCALE )

plt.axis( "off")

# cmap : color map , interpolation: 이미지의 크기 변화에 적용할 알고리즘 설정
plt.imshow( imgGRAY, cmap = "gray", interpolation = "bicubic")

# 이렇게 하면 green색이 강하다.
# plt.imshow( imgGRAY )
# plt.imshow( imgGRAY, interpolation = "bicubic")

plt.show()