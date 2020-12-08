# _*_ coding: UTF-8 _*_
# @Time     : 2020/11/30 下午 01:47
# @Author   : Li Jie
# @Site     : http://www.cdtest.cn/
# @File     : brisk_test.py
# @Software : PyCharm

import cv2
import numpy


def brisk_test():
    img = cv2.imread("lena.png")
    cv2.imshow('Input Image', img)
    cv2.waitKey(0)

    brisk = cv2.BRISK_create()
    keypoints = brisk.detect(img, None)

    # 必须要先初始化img2
    img2 = img.copy()
    img2 = cv2.drawKeypoints(img, keypoints, img2, color=(0, 255, 0))
    cv2.imshow('Detected BRISK keypoints', img2)
    cv2.waitKey(0)


if __name__ == '__main__':
    brisk_test()