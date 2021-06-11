import numpy as np
import matplotlib.pyplot as plt
import cv2
import os

background = ' ' # put background.png's location

def bluring(num, source):
    img = cv2.imread(source)
    kernel = np.ones((5, 5), np.float32)/25
    blur = cv2.filter2D(img, -1, kernel)
    cv2.imshow("blur", blur)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    # cv2.imwrite(f"./juno/bluring/{num}/{source.split('/')[4].split('.')[0]}.png", blur)

def coloring(num, source):
    img = cv2.imread(source)
    yuv_img = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)

    cv2.imshow('yuv img', yuv_img)  # color rgb -> bgr
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # color_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    # cv2.imshow('color img', color_img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    # cv2.imwrite(f"./juno/coloring/{num}/{source.split('/')[4].split('.')[0]}.png", yuv_img)

def rotate(num, source):
    image = cv2.imread(source)
    # 행과 열 정보만 저장합니다.
    height, width = image.shape[:2]

    M = cv2.getRotationMatrix2D((width / 2, height / 2), 90, 0.5)
    dst = cv2.warpAffine(image, M, (width, height))
    result = cv2.cvtColor(dst, cv2.COLOR_BGR2RGB)
    cv2.imshow('rotate', result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    # cv2.imwrite(f"./juno/rotate/{num}/{source.split('/')[4].split('.')[0]}.png", result)


def synthesis(num, source, background):
    background_image = cv2.imread(background)
    background_resize = cv2.resize(background_image, dsize=(28, 28), interpolation=cv2.INTER_AREA)
    # image resize 확인
    cv2.imshow('background_resize', background_resize)
    cv2.waitKey(0)

    # image load
    source_image = cv2.imread(source)
    result = cv2.add(source_image, background_resize)
    cv2.imshow('synthesis',result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    # cv2.imwrite(f"./juno/synthesis6/{num}/{source.split('/')[4].split('.')[0]}.png", result)

for i in range(10):
    file_dir = f"./juno/data/{i}"
    file_list = os.listdir(file_dir)
    for file in file_list:
        pass
        # coloring(i, f"{file_dir}/{file}")
        # bluring(i, f"{file_dir}/{file}")
        # synthesis(i, f"{file_dir}/{file}", background)
