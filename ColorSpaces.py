import cv2 as cv
import matplotlib.pyplot as plt

def rescaleFrame(frame, scale = 0.6):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation= cv.INTER_AREA)
first_img = cv.imread('Photos/cat2.jpg')

img = rescaleFrame(first_img)
# cv.imshow('cat',img)

plt.imshow(img)
plt.show()


# Grayscaling the image
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('cat',gray)

# BGR TO HSV / Hue Saturation Value
hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
# cv.imshow('cat',hsv)

# BGR TO LAB
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
# cv.imshow('cat',lab)

# BGR TO RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('cat',rgb)

plt.imshow(rgb)
plt.show()

cv.waitKey(0)