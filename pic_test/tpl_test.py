# _*_ coding: UTF-8 _*_
# @Time     : 2020/11/30 下午 02:22
# @Author   : Li Jie
# @Site     : http://www.cdtest.cn/
# @File     : tpl_test.py
# @Software : PyCharm

import cv2
import numpy


def surf_test():
    img = cv2.imread("lena.png")
    cv2.imshow('Input Image', img)
    cv2.waitKey(0)

    # 检测
    surf = cv2.xfeatures2d.SURF_create()
    keypoints = surf.detect(img, None)

    # 显示
    # 必须要先初始化img2
    img2 = img.copy()
    img2 = cv2.drawKeypoints(img, keypoints, img2, color=(0, 255, 0))
    cv2.imshow('Detected SURF keypoints', img2)
    cv2.waitKey(0)


if __name__ == '__main__':
    surf_test()