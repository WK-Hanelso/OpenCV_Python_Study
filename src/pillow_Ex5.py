import cv2
import os
from matplotlib import pyplot as plt
import numpy as np
from PIL import Image, ImageFilter

path = "../data/lena.jpg"

if os.path.isfile( path ) == False:
    print("no File : {}".format( path ) )
else:
    im = Image.open( path )

img2 = im.filter( ImageFilter.BLUR )
img2.show()