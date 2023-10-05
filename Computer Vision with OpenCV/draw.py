import os
import cv2 as cv
import numpy as np

blank = np.zeros((500,500, 3), dtype ='uint8') 
# implementing a new array with 500 by 500 pixels and 3 = rgb values initialization

# cv.imshow('blank', blank)

#1 painting the image a certain color

# rows : columns
blank[200:300, 300:400] = (0,255,0)   #painting the entire picture green
# cv.imshow('green', blank)

#2 Draw a rectangle
cv.rectangle(blank,(0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,255,0), thickness= -1)
# cv.imshow('rectangle', blank)

#3 draw a circle
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), radius=100, color=(255,0,0),thickness=1 )
# cv.imshow('circle', blank)

#4 draw a line
cv.line(blank, (100,250), (300,400), color=(255,255,255),thickness=1 )
# cv.imshow('line',blank)

#text on an image
cv.putText(blank, 'Hello', (255,255), cv.FONT_HERSHEY_TRIPLEX, 2.0, (0,255,0), 2)
cv.imshow('text', blank)

cv.waitKey(0)