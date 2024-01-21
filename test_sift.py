#!/usr/bin/env python
# -*- coding=utf-8 -*-
import cv2
import numpy as np

# ��ȡͼƬ,��תΪ�Ҷ�ͼ
img = cv2.imread('1111.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# ����sift����
sift = cv2.SIFT_create()
# �ؼ�����
kp = sift.detect(gray, None)
# ʹ�ùؼ��㻭ͼ
cv2.drawKeypoints(gray, kp, img)
cv2.imshow('sift', img)

cv2.waitKey(0)

