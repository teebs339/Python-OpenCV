import cv2 as cv

def rescaleFrame(frame, scale = 0.6):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation= cv.INTER_AREA)

first_img = cv.imread('Photos/cat2.jpg')
img = rescaleFrame(first_img)
# cv.imshow('cat', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('grayscale', gray)

# simple thresholding -----------------

# maxVal is 255 becuase we want to binarize the image
# no need to use the first value of the thresh we can use the second one which should be enough
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow('simple threshold', thresh)

threshold, threshinv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow('simple threshold INVERSE', threshinv)

# adaptive thresholding ----------------
# automates the threshold value so you dont have to manually change it
# value 11 and 3 were pulled outta my ass - used for 'fine tuning'

adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 3)
cv.imshow('adaptive thresholding', adaptive_thresh)

cv.waitKey(0)