import numpy as np
import cv2

filename = './file/9.png'

def bluring():
    img = cv2.imread(filename)
    kernel = np.ones((5, 5), np.float32)/25
    blur = cv2.filter2D(img, -1, kernel)
    cv2.imshow("original", img)
    cv2.imshow("blur", blur)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def coloring():
    img = cv2.imread(filename)
    yuv_img = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
    cv2.imshow('yuv img', yuv_img)  # color rgb -> bgr
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    color_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    cv2.imshow('color img', color_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

coloring()