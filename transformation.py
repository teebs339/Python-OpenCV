import cv2 as cv
import numpy as np

img = cv.imread('Photos/cat2.jpg')
cv.imshow('cat', img)

# Translate an image / move it left right and centre
def translate(img, x, y):
    transMatrix = np.array([[1, 0, x], [0, 1, y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img,transMatrix,dimensions)

# -x --> left
# -y --> up
# x --> right
# y --> down

translated = translate(img, 100, 100)
# cv.imshow('translated', translated)

# Rotation

def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2, height//2)
    
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.8)
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat,dimensions)

rotated = rotate(img, 45)
cv.imshow('rotated', rotated)

cv.destroyAllWindows()
cv.waitKey(0)