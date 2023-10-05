import cv2 as cv
import numpy as np

first_img = cv.imread('Photos/cat2.jpg')

def rescaleFrame(frame, scale = 0.6):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation= cv.INTER_AREA)

img = rescaleFrame(first_img)

blank = np.zeros(img.shape, dtype='uint8')
# cv.imshow('blank', blank)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('grayscale', gray)

blur = cv.GaussianBlur(gray,(5,5), 0)
cv.imshow('blue', blur)

canny = cv.Canny(blur, 125, 175)
cv.imshow('canny', canny)

# ret, thresh = cv.threshold(gray, 200, 255, cv.THRESH_BINARY)
# cv.imshow('thresh',thresh)

contours, hierachies = cv.findContours(canny, cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)

print(f'{len(contours)} contour(s) found! ')

cv.drawContours(blank, contours, -1, (0,0,255), 2,1)

cv.imshow('Contours drawn', blank)

cv.waitKey(0)