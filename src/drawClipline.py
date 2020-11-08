import cv2
import numpy as np

img = np.zeros( shape = ( 512, 512, 3 ), dtype = np.uint8 ) + 255

x1, x2 = 100, 400
y1, y2 = 100, 400

cv2.rectangle( img, (x1, y1), (x2, y2), (0, 0, 255 ) ) # rectangle을 x1, y1 -> x2, y2 까지 그린다.

point1 = 100, 50
point2 = 100, 500
cv2.line( img, point1, point2, (255, 0,0),2 )

# imgRect = ( x_start, y_start, x_width, y_height )
imgRect = ( x1, y1, x2-x1, y2-y1 )

# rectangle로 부터 point1 -> point2 까지의 직선과 겹치는 부분이 나오게 된다.
# 라인이 전부 겹칠 시에는 처음과 끝이 나오게 된다.
retval, rpt1, rpt2 = cv2.clipLine( imgRect, point1, point2 )
# print( rpt1, rpt2)

if retval:
    cv2.circle( img, rpt1, radius = 5, color = (0,255,0), thickness=-1 ) # -1 => fill 
    cv2.circle( img, rpt2, radius = 5, color = (0, 255, 0 ), thickness=-1 )

cv2.imshow( "img", img )
cv2.waitKey()
cv2.destroyAllWindows()

