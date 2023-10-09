from PIL import Image
import os
import cv2
import numpy as np

fPath = 'imgs/te/'
#fDistPath = 'imgs/resizing/'
fDistPath = 'imgs/resizing/'

if not os.path.exists(fDistPath):
    os.makedirs(fDistPath)

fList = os.listdir(fPath)
fList.sort()


# img 비율 유지하여 resizing & save
def setResizeImg(basewidth=600, imgPath="", imgName=""):
    img = Image.open(imgPath+imgName)
    wpercent = (basewidth / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    img_resize = img.resize((basewidth, hsize), Image.ANTIALIAS)
    img_resize.save(fDistPath+imgName+'.jpg')


def setResizeImgOpencv(sizeXY = (620, 580), imgPath="", imgName=""):
    src = cv2.imread(imgPath+imgName, cv2.IMREAD_COLOR)

    dst = cv2.resize(src, dsize=sizeXY, interpolation=cv2.INTER_AREA)
    # cv2.imshow("src", src)
    # cv2.imshow("dst", dst)

    # dst2 = cv2.resize(src, dsize=(0, 0), fx=0.3, fy=0.7, interpolation=cv2.INTER_LINEAR)
    # cv2.imshow("dst2", dst2)

    cv2.imwrite(fDistPath+imgName, dst)


size = (620, 580)
for pic in fList:
    base_pic = np.zeros((size[1], size[0], 3), np.uint8)
    pic1 = cv2.imread(fPath+pic, cv2.IMREAD_COLOR)
    h, w = pic1.shape[:2]
    ash = size[1] / h
    asw = size[0] / w
    if asw < ash:
        sizeas = (int(w * asw), int(h * asw))
    else:
        sizeas = (int(w * ash), int(h * ash))
    pic1 = cv2.resize(pic1, dsize=sizeas)
    base_pic[int(size[1] / 2 - sizeas[1] / 2):int(size[1] / 2 + sizeas[1] / 2),
    int(size[0] / 2 - sizeas[0] / 2):int(size[0] / 2 + sizeas[0] / 2), :] = pic1
    cv2.imwrite(fDistPath+pic, base_pic)

# for img in fList:
#     # setResizeImg(imgPath=fPath, imgName=img)
#     setResizeImgOpencv(imgPath=fPath, imgName=img)