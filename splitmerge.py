import cv2 as cv
import numpy as np

def rescaleFrame(frame, scale = 0.6):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation= cv.INTER_AREA)

first_img = cv.imread('Photos/cat2.jpg')
img = rescaleFrame(first_img)
# cv.imshow('cat', img)

# splits the image into blue, green and red
b,g,r = cv.split(img)
cv.imshow('blue',b)
cv.imshow('green',g)
cv.imshow('red',r)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)
 

cv.waitKey(0)