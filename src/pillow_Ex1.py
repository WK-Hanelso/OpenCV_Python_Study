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

size = ( 64, 64 )
print( im.size )
print( im.mode )

im.thumbnail( size )
print( im.size )
print( im.mode )

strOutPath = "../out/pillow_lena.jpg"

im.save( strOutPath )

