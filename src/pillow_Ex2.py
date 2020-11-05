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

img2 = im.resize( ( 800, 800 ) )
print( img2 )
print( type( img2 ) )

img2.show()



