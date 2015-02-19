import cv2
import cv2.cv as cv
print cv.CV_CAP_OPENNI
n = 0
while n < 10000:
	try:
		capture = cv2.VideoCapture(n)
		print n
	except:
		pass
	n = n + 1

	# capture.set(cv.CV_CAP_OPENNI_IMAGE_GENERATOR_OUTPUT_MODE, cv.CV_CAP_OPENNI_VGA_30HZ)

	# if capture.get(cv.CV_CAP_PROP_OPENNI_REGISTRATION) == 0: # set depth to calibrate automatically
	# 	capture.set(cv.CV_CAP_PROP_OPENNI_REGISTRATION,1)

	# print capture.grab()
	# n = n + 1