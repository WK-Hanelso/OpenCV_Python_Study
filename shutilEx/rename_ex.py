import os
strNewName = ""
nCount = 0
strPath = "./data/dogs"
strBaseDir = "./data/dogs/"
fileList = os.listdir( strPath )

print( fileList )

for strTmp in fileList:
    nCount += 1
    # print( strTmp )
    strNewName = "dog" + str( nCount ) + ".jpeg"
    os.rename( strBaseDir + strTmp, strBaseDir + strNewName )

fileList = os.listdir( strPath )
print( fileList )
