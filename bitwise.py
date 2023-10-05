# BITWISE TO MERGE TWO DIFFERENT SHIT TOGETHER
import cv2 as cv
import numpy as np

blank = np.zeros([400,400] , dtype= 'uint8')

rectangle = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1)
circle = cv.circle(blank.copy(), (200,200), 200, (255,255,255), -1)

cv.imshow('rectangle', rectangle)
cv.imshow('cirlce', circle)

# bitwise AND
bitwise_and = cv.bitwise_and(rectangle, circle)
cv.imshow('bitwise and', bitwise_and)

# bitwise OR
bitwise_or = cv.bitwise_or(rectangle, circle)
cv.imshow('bitwise or', bitwise_or)



cv.waitKey(0)