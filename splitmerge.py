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

# used to create a blank image of the same size as the cat image 
blank = np.zeros(img.shape[0:2], dtype= 'uint8')


# splits the image into blue, green and red
b,g,r = cv.split(img)

blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])

cv.imshow('blue',blue)
cv.imshow('green',green)
cv.imshow('red',red)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

merge = cv.merge([b,g,r])
cv.imshow('merged image', merge)

cv.waitKey(0)