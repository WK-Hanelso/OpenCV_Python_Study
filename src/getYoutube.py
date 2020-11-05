import cv2
import os
from matplotlib import pyplot as plt
# youtube 영상을 파싱해주는 모듈
import pafy         

url = "https://www.youtube.com/watch?v=kIBxM0WdWlE"
video = pafy.new( url )
print( video )
# print( type( video ))

# 카메라를 사용할 경우 파일 경로명을 입력해줘야할 위치에 
# 카메라 번호를 설정해주면 된다.
best = video.getbest( preftype="mp4")
print( best )
print( type( best ) )
cap = cv2.VideoCapture( best.url )

# 동영상 크기( frame 정보 )를 읽어온다.
frameWidth = int( cap.get( cv2.CAP_PROP_FRAME_WIDTH))
frameHeight = int( cap.get( cv2.CAP_PROP_FRAME_HEIGHT) )
framePerSec = int( cap.get( cv2.CAP_PROP_FPS) )

frame_size = ( frameWidth, frameHeight )
print( "frmae_size, fps  = {},{}".format( frame_size, framePerSec ) )

# codec 및 녹화 관련 설정
fourcc = cv2.VideoWriter_fourcc(*"XVID")
# fourcc = cv2.VideoWriter_fourcc(*"DIVX")
# fourcc = cv2.VideoWriter_fourcc(*"MPEG")
# fourcc = cv2.VideoWriter_fourcc(*"X264")

strTmp1Path = "../out/record1.mp4"
strTmp2Path = "../out/record2.mp4"
out1 = cv2.VideoWriter( strTmp1Path, fourcc, framePerSec, frame_size )
out2 = cv2.VideoWriter( strTmp2Path, fourcc, framePerSec, frame_size )

# 동영상 프레임을 캡쳐
while True:
    # 한 장의 이미지를 가져온다.
    # 이미지 -> frame
    # 정상적으로 읽어왔는지 -> retval ( 프레임 정보를 정상적으로 읽지 못하면 while문을 빠져 나온다. )
    retval, frame = cap.read()
    if retval == False:
        break

    gray = cv2.cvtColor( frame, cv2.COLOR_BGR2GRAY )
    edges = cv2.Canny(gray, 100, 200 )

    # 동영상 파일에 쓰기
    out1.write( frame )
    out2.write( edges )

    # 동영상 모니터에 출력
    cv2.imshow("frame", frame )
    cv2.imshow('edges', edges )

    key = cv2.waitKey(33) # 33 milli sec 동안 1개의 프레임 ( 초당 30 frame )

    # key 가 27이 눌리면
    if key == 27:
        break

# cap 이 열려 있다면 
if cap.isOpened():
    # cap을 해제
    cap.release()
    out1.release()
    out2.release()

# 모든 cv2 위도우들을 제거한다.
cv2.destroyAllWindows()


