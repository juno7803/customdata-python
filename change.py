import numpy as np
import matplotlib.pyplot as plt
import cv2

filename = './file/9.png'
background_1 = './file/background_1.png'

def bluring(source):
    img = cv2.imread(source)
    kernel = np.ones((5, 5), np.float32)/25
    blur = cv2.filter2D(img, -1, kernel)
    cv2.imshow("original", img)
    cv2.imshow("blur", blur)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def coloring(source):
    img = cv2.imread(source)
    yuv_img = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
    cv2.imshow('yuv img', yuv_img)  # color rgb -> bgr
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    color_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    cv2.imshow('color img', color_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def rotate(source):
    image = cv2.imread(source)
    # 행과 열 정보만 저장합니다.
    height, width = image.shape[:2]

    M = cv2.getRotationMatrix2D((width / 2, height / 2), 90, 0.5)
    dst = cv2.warpAffine(image, M, (width, height))

    plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))
    plt.show()

def synthesis(source, background):
    background_image = cv2.imread(background)
    background_resize = cv2.resize(background_image, dsize=(28, 28), interpolation=cv2.INTER_AREA)
    # image resize 확인
    cv2.imshow('background_resize', background_resize)
    cv2.waitKey(0)

    # image load
    source_image = cv2.imread(source)

    result = cv2.add(source_image, background_image)
    plt.imshow(cv2.cvtColor(result, cv2.COLOR_BGR2RGB))
    plt.show()

# bluring(filename)
# rotate(filename)
# coloring(filename)
# synthesis(filename, background_1)