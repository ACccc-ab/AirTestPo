# _*_ coding: UTF-8 _*_
# @Time     : 2020/11/30 下午 01:56
# @Author   : Li Jie
# @Site     : http://www.cdtest.cn/
# @File     : orb_test.py
# @Software : PyCharm


import cv2
import numpy


def orb_test():
    img = cv2.imread("lena.png")
    cv2.imshow('Input Image', img)
    cv2.waitKey(0)

    # 检测
    orb = cv2.ORB_create()
    keypoints = orb.detect(img, None)

    # 显示
    # 必须要先初始化img2
    img2 = img.copy()
    img2 = cv2.drawKeypoints(img, keypoints, img2, color=(0, 255, 0))
    cv2.imshow('Detected ORB keypoints', img2)
    cv2.waitKey(0)


if __name__ == '__main__':
    orb_test()