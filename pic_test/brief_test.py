# _*_ coding: UTF-8 _*_
# @Time     : 2020/11/30 下午 02:04
# @Author   : Li Jie
# @Site     : http://www.cdtest.cn/
# @File     : brief_test.py
# @Software : PyCharm

import cv2
import numpy


def brief_test():
    img = cv2.imread("lena.png")
    cv2.imshow('Input Image', img)
    cv2.waitKey(0)

    # OpenCV3.x
    # 注意由star计算特征点，brief进行简化
    star = cv2.xfeatures2d.StarDetector_create()
    brief = cv2.xfeatures2d.BriefDescriptorExtractor_create()

    """获取图像特征点和描述符."""
    # find the keypoints with STAR
    keypoints = star.detect(img, None)
    # compute the descriptors with BRIEF
    keypoints, descriptors = brief.compute(img,keypoints)

    # 必须要先初始化img2
    img2 = img.copy()
    img2 = cv2.drawKeypoints(img, keypoints, img2, color=(0, 255, 0))
    cv2.imshow('Detected brief keypoints', img2)
    cv2.waitKey(0)


if __name__ == '__main__':
    brief_test()
