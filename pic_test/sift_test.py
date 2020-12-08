# _*_ coding: UTF-8 _*_
# @Time     : 2020/11/30 上午 11:49
# @Author   : Li Jie
# @Site     : http://www.cdtest.cn/
# @File     : sift_test.py
# @Software : PyCharm


import cv2
import numpy


def sift_test():
    img = cv2.imread("lena.png")
    cv2.imshow('Input Image', img)
    cv2.waitKey(0)

    # 检测
    sift = cv2.xfeatures2d.SIFT_create()
    keypoints = sift.detect(img, None)

    # 显示
    # 必须要先初始化img2
    img2 = img.copy()
    img2 = cv2.drawKeypoints(img, keypoints, img2, color=(0, 255, 0))
    cv2.imshow('Detected SIFT keypoints', img2)
    cv2.waitKey(0)


if __name__ == '__main__':
    sift_test()