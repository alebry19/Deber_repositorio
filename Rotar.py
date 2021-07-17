import cv2
import numpy as np
import os
import glob
import imutils


path = os.getcwd()


original = "\crop"

imgPro = "\p"

filenames = glob.glob(path+original+"\*.jpg")

dim = (24,24)

numImg = 1

stepGrados = 60

for filename in filenames:
    img = cv2.imread(filename)
    for k in range(0,360,stepGrados):
        rotated = imutils.rotate_bound(img,k)
        resized = cv2.resize(rotated,dim,interpolation = cv2.INTER_AREA)
        cv2.imwrite(path+imgPro+"\positivo("+str(k)+"_"+str(numImg)+").jpg",resized)
    numImg = numImg+1
    
