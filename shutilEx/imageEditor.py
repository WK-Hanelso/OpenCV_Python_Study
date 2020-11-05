import cv2
import os
from matplotlib import pyplot as plt
import numpy as np
from PIL import Image, ImageFilter


def actResize( srcImg, strDirPath ):
    objImg = cv2.resize( srcImg, dsize = ( 0, 0 ), fx=0.8, fy=0.2, interpolation = cv2.INTER_AREA )
    return objImg

def actRotate( srcImg, strDirPath ):
    ( height, width ) = srcImg.shape[:2]
    center = ( width/2, height/2 )
    matrix = cv2.getRotationMatrix2D( center, 180, 1.0 )
    objImg = cv2.warpAffine( srcImg, matrix, (width, height ) )
    return objImg

def actBlur( srcImg, strDirPath ):
    objImg = cv2.blur( srcImg, ( 3, 3 ) )
    return objImg

def actCrop( srcImg, strDirPath ):
    ( height, width ) = srcImg.shape[:2]
    if width < height:
        value = width

    else:
        value = height
    
    objImg = srcImg[0:value, 0:value]
    return objImg


if __name__=="__main__":

    dictFunc = {'1': actResize , '2': actRotate ,'3': actBlur, '4': actCrop }
    strDirPath = "./data/dogs"

    # 디렉토리 읽어오기
    if os.path.isdir( strDirPath ) == False:
        print( "no Dir : {}".format( strDirPath ) )
    else:
        listFiles = os.listdir( strDirPath )
    # print( listFiles )


    # 파일 읽어서 동작 수행하기
    for strFileName in listFiles:
        strFilePath = os.path.join( strDirPath, strFileName )
        # print( strFilePath )

        if os.path.isfile( strFilePath ) == False:
            print( "no file : {}".format( strFilePath ) )
            break
        else:
            srcImg = cv2.imread( strFilePath )

        strQues = '''
        기능 : 원하는 번호들을 빈칸으로 구분해서 넣어주세요!
        1. 파일 크기 재조정
        2. 파일 돌리기
        3. 파일 Blur하기
        4. 파일 자르기
        원하는 기능 : 
        '''
        strTmp = input( strQues )

        listSelects = strTmp.split(" ")
        # print( listSelects )

        # 동작 수행하기
        objImg = srcImg
        # cv2.imshow( "original", srcImg)
        for strSelect in listSelects:
            dstImg = dictFunc[strSelect]( objImg, strFilePath )
            objImg = dstImg
            # cv2.imshow( strSelect, objImg )
            # cv2.waitKey()

        # cv2.destroyAllWindows()
        
        # 파일 저장하기
        strOutDirPath = "./data/out"
        if os.path.isdir( strOutDirPath ) == False:
            print( "no Dir : {}". format( strOutDirPath ) )
        else:
            strOutFilePath = os.path.join( strOutDirPath, "changed_" + strFileName )
            cv2.imwrite( strOutFilePath, objImg )

    print(" end")