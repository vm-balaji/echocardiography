
import cv2
import os
import re
import json
#from pylab import *
#from PIL import Image, ImageChops, ImageEnhance

train_frame_folder = 'Video/Rhabdomyoma'

count = 0
cap = cv2.VideoCapture('Video/Rhabdomyoma/0X1EE30D34D1CBF56A.avi')
    #frameRate = cap.get(5)
while cap.isOpened():
    frameId = cap.get(1)
    ret, frame = cap.read()
    cv2.imwrite('Dataset/Rhabdomyoma/' +'0X1EE30D34D1CBF56A' + str(count) + '.png', cv2.resize(frame, (200, 200),interpolation=cv2.INTER_AREA))
    count += 1
    if ret != True:
        break


