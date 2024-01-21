#!/usr/bin/env python
# -*- coding=utf-8 -*-
import cv2
import numpy as np

# 读取图片,并转为灰度图
img = cv2.imread('1111.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 创建sift对象
sift = cv2.SIFT_create()
# 关键点检测
kp = sift.detect(gray, None)
# 使用关键点画图
cv2.drawKeypoints(gray, kp, img)
cv2.imshow('sift', img)

cv2.waitKey(0)

