import cv2
import os
from matplotlib import pyplot as plt
import numpy as np
from PIL import Image, ImageFilter

path = "../data/lena.jpg"

if os.path.isfile( path ) == False:
    print("no File : {}".format( path ) )
else:
    img = cv2.imread( path )

size = ( 256, 256 )

# img를 size 크기로 다시 만드는데 INTER_AREA 방식( 전체적으로 작게 )
dst = cv2.resize( img, dsize=size, interpolation = cv2.INTER_AREA )

# img를 (0,0)사이즈( 0이 아니고 미지정 )인데 x 기준 0.8( 80% ), y 기준 0.2( 20% )로 INTER_AREA 방식이다.
dst2 = cv2.resize( img, dsize=(0,0), fx=0.8, fy=0.2, interpolation = cv2.INTER_AREA )

cv2.imshow("src", img )
cv2.imshow("dst", dst )
cv2.imshow("dst2", dst2 )

cv2.waitKey()
cv2.destroyAllWindows()