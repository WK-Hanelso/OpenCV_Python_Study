import cv2
import numpy as np

# numpy.zeros 로 생성되는 shape 모양은 행렬의 형태를 띄고 있다. 따라서 + 연산을 하면 행렬 전체에 합연산이된다.
# White 배경 생성
img = np.zeros( shape = (512, 512, 3 ), dtype=np.uint8 ) + 255 # 3개의 채널을 모두 255로 채운다.
# img2 = np.zeros( shape = (512, 512, 3 ), dtype=np.uint8 ) + 1
# img3 = np.ones( (512, 512, 3 ), np.uint8 ) * 255 # 3개의 채널을 모두 255로 채운다.
# img4 = np.full( (512,512,3), (255,255,255), dtype=np.uint8 ) # 3차원 행렬을 255, 255,255로 채운다.

# print( img )
# print( type(img ) )

# print( img2 )
# print( type(img2 ) )

# print( img3 )
# print( type(img3 ) )

# print( img4 )
# print( type( img4 ) )

point1 = 100, 100
point2 = 400, 400

# point1 과 정반대 지점인 point2로 rectangle을 그리는데 색은 (0,255,0)이고, 두께는 2이다. ( linetype도 정할 수 있다.)
# cv2.rectangle(img, pt1 = point1, pt2 = point2, color=(0, 255, 0), thickness=2 )
cv2.rectangle(img, point1, point2, (0, 255, 0), 2 )

cv2.line( img, pt1 = ( 0, 0 ), pt2 = ( 500, 0 ), color = ( 255, 0, 0 ), thickness = 10 )
cv2.line( img, pt1 = ( 0, 0 ), pt2 = ( 0, 500 ), color = ( 0, 0, 255 ), thickness = 10 )

cv2.imshow( "img", img )
cv2.waitKey()
cv2.destroyAllWindows()