import cv2
import numpy
 
def main():
	img = cv2.imread("1111.png")
	cv2.imshow('Input Image', img)
	cv2.waitKey(0)
 
 
	brisk = cv2.BRISK_create()
	keypoints = brisk.detect(img, None)
	

	img2 = img.copy()
	img2 = cv2.drawKeypoints(img, keypoints, img2, color=(0,255,0))
	# cv2.imwrite('brisk.png', img2)
	cv2.imshow('Detected BRISK keypoints', img2)
	cv2.waitKey(0)
    
if __name__ == '__main__':
	main()
