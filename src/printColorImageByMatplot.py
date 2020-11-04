import cv2
import os 

# matplotlib 패키지는 matrix plot(그리다) library로 matrix처럼 그리는 라이브러리이다.
# pyplt는 python으로 그리는 모듈이다.
from matplotlib import pyplot as plt

imageFile = "../data/lena.jpg"

# File이 존재하는지 확인하는 코드
if os.path.isfile( imageFile ) == False:
    print("no File : {}".format( imageFile ) )

# BGR 포맷으로 읽힌다.
imgBGR = cv2.imread( imageFile )

plt.axis("off")

# plot에 그리기 우해서는 RGB 순서의 포맷이어야 원본의 값을 그대로 가져올 수 있다.
imgRGB = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2RGB )

# pyplot은 이미지 정보를 plt에 그리고 show()를 통해서 보여준다.
plt.imshow(imgRGB)
plt.show()

plt.imshow(imgBGR)
plt.show()
