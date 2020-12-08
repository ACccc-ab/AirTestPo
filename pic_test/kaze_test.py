# _*_ coding: UTF-8 _*_
# @Time     : 2020/11/30 下午 01:52
# @Author   : Li Jie
# @Site     : http://www.cdtest.cn/
# @File     : kaze_test.py
# @Software : PyCharm


import cv2
import numpy


def kaze_test():
    img = cv2.imread("lena.png")
    cv2.imshow('Input Image', img)
    cv2.waitKey(0)

    # 检测
    kaze = cv2.KAZE_create()
    keypoints = kaze.detect(img, None)

    # 显示
    # 必须要先初始化img2
    img2 = img.copy()
    img2 = cv2.drawKeypoints(img, keypoints, img2, color=(0, 255, 0))
    cv2.imshow('Detected KAZE keypoints', img2)
    cv2.waitKey(0)


if __name__ == '__main__':
    kaze_test()
