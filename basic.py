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
blurred_img = cv.GaussianBlur(gray, (7, 7), 0)
# cv.imshow('blurred', blurred_img)

# edge cascading / edge detection
canny = cv.Canny(blurred_img, 123,175)
# cv.imshow('canny', canny)

# dilating the image
dilated = cv.dilate(canny, (7,7), iterations= 1 )
# cv.imshow('dialted', dilated)

# Eroding
eroded = cv.erode(dilated, (3,3))
# cv.imshow('eroded', eroded)

# Resize
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
# cv.imshow('resized', resized)

# Cropping
cropped = img[50:250, 200:400]
cv.imshow('cropped', cropped)

cv.waitKey(0)