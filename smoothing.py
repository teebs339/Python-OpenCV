#smoothing is used for removing noise in an image

import cv2 as cv
import numpy as np

def rescaleFrame(frame, scale = 0.6):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation= cv.INTER_AREA)

first_img = cv.imread('Photos/cat2.jpg')
img = rescaleFrame(first_img)
cv.imshow('cat',img)

# averaging
# (3, 3) is the kernel or the amount of blur you want
average = cv.blur(img, (3,3))
cv.imshow('blur', average)

# gaussian blur
gauss = cv.GaussianBlur(img, (3,3), 0)
cv.imshow('gaussian blur', gauss)

# median blur
median = cv.medianBlur(img, 3)
cv.imshow('median blur', median)

# bilateral blur / the best one in CV
bilateral = cv.bilateralFilter(img, 15, 35, 25)
cv.imshow('bilateral blur', bilateral)

cv.waitKey(0)