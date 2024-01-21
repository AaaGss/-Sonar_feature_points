#!/usr/bin/env python
# -*- coding=utf-8 -*-
# Summary: ʹ��OpenCV3.x-Python���AKAZE������
# Author:  Amusi
# Date:    2018-03-17
# Reference: https://docs.opencv.org/master/d8/d30/classcv_1_1AKAZE.html
# Reference: https://blog.csdn.net/luoganttcc/article/details/121512859?spm=1001.2014.3001.5506
 
import cv2
import numpy
 
def main():
 
	img = cv2.imread("1111.png")
	cv2.imshow('Input Image', img)
	cv2.waitKey(0)
	
	# ���
	akaze = cv2.AKAZE_create()
	keypoints = akaze.detect(img, None)
	
	# ��ʾ
	# ����Ҫ�ȳ�ʼ��img2
	img2 = img.copy()
	img2 = cv2.drawKeypoints(img, keypoints, img2, color=(0,255,0))
	cv2.imshow('Detected AKAZE keypoints', img2)
	cv2.waitKey(0)
    
if __name__ == '__main__':
	main()
