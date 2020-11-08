import cv2
import numpy as np

# 512, 512 사이즈의 3채널의 컬러 화면을 255로채워서 넣어라! ( 흰 바탕 )
img = np.zeros( shape = ( 512, 512, 3 ), dtype = np.uint8 ) + 255

pointCenter = img.shape[0] // 2 , img.shape[1] // 2
size = 200, 100

# 타원을 그린다. 
# cv2.ellipse( 
#     src = img, 
#     center = pointCenter, 
#     axes = size, 
#     angle = 0, 
#     startAngle = 0, 
#     endAngle = 360, 
#     color = ( 255, 0, 0 )
# )
cv2.ellipse( img, pointCenter, size, 0, 0, 360, ( 255, 0, 0 ) )
cv2.ellipse( img, pointCenter, size, 45, 0, 360, ( 0, 0, 255 ) )

# box = ( center = pointCenter, axes = size, angle = 0 )
box = ( pointCenter, size, 0 )
# default로 startAngle = 0, endAngle = 360 인듯....
cv2.ellipse( img, box, ( 255, 0, 0 ), 5 )

box = ( pointCenter, size, 45 )
cv2.ellipse( img, box, ( 0, 0, 255 ), 5 )

cv2.imshow( "img", img )
cv2.waitKey()
cv2.destroyAllWindows()