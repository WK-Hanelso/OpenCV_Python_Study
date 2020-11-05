import cv2
import os
from matplotlib import pyplot as plt

dirPath = "../data"
filePath = os.path.join( dirPath, "vtest.avi")

# File이 존재하는지 확인하는 코드
if os.path.isfile( filePath ) == False:
    print("no Dir : {}".format( filePath ) )
else:
    cap = cv2.VideoCapture( filePath )
    print( cap )

# 동영상 크기( frame 정보 )를 읽어온다.
frameWidth = int( cap.get(cv2.CAP_PROP_FRAME_WIDTH) )
frameHeight = int( cap.get( cv2.CAP_PROP_FRAME_HEIGHT) )

frmae_size = ( frameWidth, frameHeight )
print( "frmae_size = {}".format( frmae_size ) )

# 동영상 프레임을 캡쳐
while True:
    # 한 장의 이미지를 가져온다.
    # 이미지 -> frame
    # 정상적으로 읽어왔는지 -> retval ( 프레임 정보를 정상적으로 읽지 못하면 while문을 빠져 나온다. )
    retval, frame = cap.read()
    if retval == False:
        break

    cv2.imshow("frame", frame )
    key = cv2.waitKey(33) # 33 milli sec 동안 1개의 프레임 ( 초당 30 frame )

    # key 가 27이 눌리면
    if key == 27:
        break

# cap 이 열려 있다면 
if cap.isOpened():
    # cap을 해제
    cap.release()

# 모든 cv2 위도우들을 제거한다.
cv2.destroyAllWindows()


