import cv2 as cv
import numpy as np

first_img = cv.imread('Photos/cat2.jpg')

def rescaleFrame(frame, scale = 0.6):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation= cv.INTER_AREA)

img = rescaleFrame(first_img)
cv.imshow('cat', img)

#make sure that mask is the same size as of the target image
blank = np.zeros(img.shape[0:2], dtype= 'uint8')
# cv.imshow('blank image', blank)

height = img.shape[0]//2
width = img.shape[1]//2

mask = cv.circle(blank, (width, height), 200, (255,255,255), -1)
cv.imshow('mask', mask)

# THE MAIN MASKING KEY
masked = cv.bitwise_and(img, img, mask= mask)
cv.imshow('masked image', masked)

cv.waitKey(0)