import cv2 as cv
import numpy as np

def rescaleFrame(frame, scale = 0.6):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation= cv.INTER_AREA)

f_img = cv.imread('Photos/cat2.jpg')
img = rescaleFrame(f_img)
# cv.imshow('img', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

# laplacing method

lap = cv.Laplacian(gray, cv.CV_8U)
lap = np.uint8(np.absolute(lap))
cv.imshow('laplace', lap)

cv.waitKey(0)