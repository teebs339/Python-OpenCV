import cv2 as cv

def rescaleFrame(frame, scale = 0.6):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation= cv.INTER_AREA)

f_img = cv.imread('Photos/cat2.jpg')
img = rescaleFrame(f_img)
cv.imshow('img', img)

cv.waitKey(0)