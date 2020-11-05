import cv2
import os
from matplotlib import pyplot as plt
import numpy as np

path = "../data/lena.jpg"

if os.path.isfile( path ) == False:
    print("no File : {}".format( path ) )
else:
    src = cv2.imread( path )
    srcGray = cv2.imread( path, 0 ) # cv2.IMREAD_GRAYSCALE == 0


b, g, r = cv2.split( src )
# print( src )
print( srcGray )
print( srcGray.shape )

# 이미지 파일( 컬러 )는 width, height, channel을 갖는 정보이다.
height, width, channel = src.shape
print( height, width, channel )

# r, g, b 는 각 색의 채널이 wid와 height만 가지고 있다.
height, width = g.shape
print( height, width)

height, width = r.shape
print( height, width)

height, width = b.shape
print( height, width)

# numpy( np )를 이용해서 height, width, 1칸 의 배열을 만든다. ( 모두 0으로 채워져 있다. ) 
# 해당 소스 코드에서는 마지막 1이라고 넣어준 channel에 대응하는 부분은 제거해도 된다.
zero = np.zeros( (height, width, 1 ), dtype = np.uint8 )
print( zero.shape)
height, width, channel = zero.shape
print( height, width, channel )

# 각 이미지 channel 값으로 새로운 칼라( 3channel )이미지를 생성
imgB = cv2.merge( ( b, zero, zero ) )
imgR = cv2.merge( ( zero, zero, r ) )
imgG = cv2.merge( ( zero, g, zero ) )

cv2.imshow('b', imgB )

cv2.waitKey()
cv2.destroyAllWindows()