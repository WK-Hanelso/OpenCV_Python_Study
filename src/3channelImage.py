import cv2
import os
from matplotlib import pyplot as plt

path = "../data/lena.jpg"

if os.path.isfile( path ) == False:
    print("no File : {}".format( path ) )
else:
    src = cv2.imread( path )
    srcGray = cv2.imread( path, 0 ) # cv2.IMREAD_GRAYSCALE == 0

# print( src )
# print( type( src ) )

# channel 별로 image 를 분리
b, g, r = cv2.split( src )
# imgBGR = cv2.merge( (r,g,b) )
imgRGB = cv2.merge( (b,g,r) )
imgBGRGray = cv2.merge( ( srcGray, srcGray, srcGray ) )

cv2.imshow( "b", b )
cv2.imshow( "g", g )
cv2.imshow( "r", r )

cv2.imshow( "imgBGR", imgRGB )
cv2.imshow( "img3Gray", imgBGRGray )

cv2.waitKey()
cv2.destroyAllWindows()