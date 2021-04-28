""" This script accesses to pixels values of an image.
It draws a rectagle from a quarter to three-quarters
in rows and colums """
import cv2

IMGNAME = 'cat_01.jpg'

img = cv2.imread(IMGNAME)
imgRows, imgColumns, imgChannels= img.shape

for i in range(imgRows//4, (imgRows//4)*3):
    for j in range(imgColumns//4, (imgColumns//4)*3):
        img.itemset((i, j, 0), 0)
        img.itemset((i, j, 1), 0)
        img.itemset((i, j, 2), 0)

cv2.imshow('Cat', img)
cv2.waitKey(0)
