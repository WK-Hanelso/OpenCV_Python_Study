import cv2
import os
from matplotlib import pyplot as plt

path = "../data"
imageFile1 = "../data/lena.jpg"
imageFile2 = "../data/apple.jpg"
imageFile3 = "../data/baboon.jpg"
imageFile4 = "../data/orange.jpg"

# File이 존재하는지 확인하는 코드
if os.path.isdir( path ) == False:
    print("no Dir : {}".format( path ) )
else:
    imgBGR1 = cv2.imread( imageFile1 )
    imgBGR2 = cv2.imread( imageFile2 )
    imgBGR3 = cv2.imread( imageFile3 )
    imgBGR4 = cv2.imread( imageFile4 )

imgRGB1 = cv2.cvtColor( imgBGR1, cv2.COLOR_BGR2RGB )
imgRGB2 = cv2.cvtColor( imgBGR2, cv2.COLOR_BGR2RGB )
imgRGB3 = cv2.cvtColor( imgBGR3, cv2.COLOR_BGR2RGB )
imgRGB4 = cv2.cvtColor( imgBGR4, cv2.COLOR_BGR2RGB )

# subplot( 2행 2열로 된 이미지 4개를 띄우기 위해 )
# 전체 사이즈 ( 10 x 10 )
fig, ax = plt.subplots(2,2, figsize = (10, 10 ), sharey= True )

print( fig )
print( ax )

# fig -> 창의 이름을 설정
fig.canvas.set_window_title( "Sample Pictures" )

ax[0][0].axis("off")
ax[0][1].axis("off")
ax[1][0].axis("off")
ax[1][1].axis("off")

# aspect : 가로 세로 비율을 auto로 설정한다.
ax[0][0].imshow( imgRGB1, aspect="auto")
# ax[0][0].imshow( imgRGB1)
ax[0][1].imshow( imgRGB2, aspect="auto")
ax[1][0].imshow( imgRGB3, aspect="auto")
ax[1][1].imshow( imgRGB4, aspect="auto")

dstName = "./myFig.png"
plt.subplots_adjust( left = 0, bottom = 0, right = 1, top = 1, wspace = 0.05, hspace=0.05)
plt.savefig( dstName, bbox_inces = "tight" )
plt.show()

