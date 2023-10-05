import cv2 as cv

def rescaleFrame(frame, scale = 0.6):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation= cv.INTER_AREA)


first_img = cv.imread('Photos/cat2.jpg')
img = rescaleFrame(first_img)
# coverting into grayscale image

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('gray',gray)

# blurring an image
blurred_img = cv.GaussianBlur(gray, (3, 101), 0)
cv.imshow('blurred', blurred_img)

cv.waitKey(0)