import cv2
import os
from matplotlib import pyplot as plt
import numpy as np
from PIL import Image

path = "../data/lena.jpg"

if os.path.isfile( path ) == False:
    print("no File : {}".format( path ) )
else:
    im = Image.open( path )

# 512 x 512 ==> (100, 100 ) 부터 ( 350, 350 )까지 자르겠다.
img2 = im.crop( ( 100, 100, 350, 350 ) )

img2.show()