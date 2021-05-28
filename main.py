import cv2
import os
import numpy as np

filenames = ['13.jpg', '14.jpg', '15.jpg']

def generate_dataset(filename):
    src = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)  # 그레이 스케일로 변환
    src = cv2.resize(src, (int(src.shape[1] / 5), int(src.shape[0] / 5)))  # 이미지의 크기가 워낙 크기 때문에 5분의1로 줄여서 확인
    cv2.imshow('gray', src)
    k = cv2.waitKey(0)
    cv2.destroyAllWindows()

    src = src[0:src.shape[0] - 10, 15:src.shape[1] - 25]  # 양 옆의 노이즈를 제거
    ret, binary = cv2.threshold(src, 170, 255, cv2.THRESH_BINARY_INV)  # 영상 이진화

    cv2.imshow('binary', binary)
    k = cv2.waitKey(0)
    cv2.destroyAllWindows()

    # binary = cv2.morphologyEx(binary , cv2.MORPH_OPEN , cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2,2)), iterations = 2)
    # cv2.imshow('binary',binary)
    # k = cv2.waitKey(0)
    # cv2.destroyAllWindows()

    contours, hierarchy = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)  # 외곽선 검출
    color = cv2.cvtColor(binary, cv2.COLOR_GRAY2BGR)  # 이진화 이미지를 color이미지로 복사(확인용)
    cv2.drawContours(color, contours, -1, (0, 255, 0), 3)  # 초록색으로 외곽선을 그려준다.

    # 리스트연산을 위해 초기변수 선언
    bR_arr = []
    digit_arr = []
    digit_arr2 = []
    count = 0

    # 검출한 외곽선에 사각형을 그려서 배열에 추가
    for i in range(len(contours)):
        bin_tmp = binary.copy()
        x, y, w, h = cv2.boundingRect(contours[i])
        bR_arr.append([x, y, w, h])

    bR_arr = sorted(bR_arr, key=lambda num: num[0], reverse=False)

    print(bR_arr[:5])
    print(len(bR_arr))

    # 작은 노이즈데이터 버림,사각형그리기, 10개씩 리스트로 다시 묶어서 저장
    for x, y, w, h in bR_arr:
        tmp_y = bin_tmp[y - 2:y + h + 2, x - 2:x + w + 2].shape[0]
        tmp_x = bin_tmp[y - 2:y + h + 2, x - 2:x + w + 2].shape[1]
        if tmp_x and tmp_y > 10:
            count += 1
            cv2.rectangle(color, (x - 2, y - 2), (x + w + 2, y + h + 2), (0, 0, 255), 1)
            digit_arr.append(bin_tmp[y - 2:y + h + 2, x - 2:x + w + 2])
            if count == 10:
                digit_arr2.append(digit_arr)
                digit_arr = []
                count = 0
    cv2.imshow('contours', color)

    k = cv2.waitKey(0)
    cv2.destroyAllWindows()

    for i in range(0, len(digit_arr2)):
        for j in range(len(digit_arr2[i])):
            count += 1
            if i == 0:  # 1일 경우 비율 유지를 위해 마스크를 만들어 그위에 얹어줌
                width = digit_arr2[i][j].shape[1]
                height = digit_arr2[i][j].shape[0]
                tmp = (height - width) / 2
                mask = np.zeros((height, height))
                mask[0:height, int(tmp):int(tmp) + width] = digit_arr2[i][j]
                digit_arr2[i][j] = cv2.resize(mask, (28, 28))
            else:
                digit_arr2[i][j] = cv2.resize(digit_arr2[i][j], (28, 28))
            # if i == 9 : i = -1
            cv2.imwrite(f"./juno/data/{i}/" + str(i) + '_' + str(j) + f"_{filename.split('.')[0]}.png", digit_arr2[i][j])

for filename in filenames:
    generate_dataset(filename)

# def createdataset(directory): #sklearn사용을 위해 데이터세트를 생성
#     files = os.listdir(directory)
#     x = []
#     y = []
#     for file in files:
#         attr_x = cv2.imread(directory+file, cv2.IMREAD_GRAYSCALE)
#         attr_x = attr_x.flatten()
#         attr_y = file[0]
#         x.append(attr_x)
#         y.append(attr_y)
#
#         x = np.array(x)
#         y = np.array(y)
#         return x , y
#
# train_dir = './juno/data/'
# train_x ,train_y = createdataset(train_dir)
# test_dir = './juno/test/'
# test_x , test_y = createdataset(test_dir)
