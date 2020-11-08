import cv2
import numpy as np


img = np.zeros( shape = ( 512, 512, 3 ), dtype = np.uint8 ) + 255
cx = img.shape[0] // 2   # 원 중심의 x 좌표
cy = img.shape[1] // 2   # 원 중심의 y 좌표

for r in range( 200, 0, -100 ):
    # 원을 그리는데 
    cv2.circle( img, ( cx, cy ), r, color = ( 255, 0, 0 ) )

cv2.circle( img, ( cx, cy ), radius = 50, color = ( 0, 0, 255 ), thickness = -1 )
# cv2.circle( img, ( cx, cy ), radius = 50, color = ( 0, 0, 255 ), thickness = 100 )

cv2.imshow( "img", img )
cv2.waitKey()
cv2.destroyAllWindows()