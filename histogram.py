import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

def rescaleFrame(frame, scale = 0.6):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation= cv.INTER_AREA)

first_img = cv.imread('Photos/cat2.jpg')
img = rescaleFrame(first_img)
cv.imshow('cat', img)

blank = np.zeros(img.shape[0:2], dtype= 'uint8')

#grayscale histogram ----------------

# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)



# mask = cv.bitwise_and(gray, gray, mask=circle)
# cv.imshow('mask', mask)

# grayscale histogram / compute the histogram for the imagine that is passed. image is in list so we pass a list into the function

# gray_histogram = cv.calcHist([gray], [0], mask, [256], [0, 256])

# plt.figure()    #instantiate
# plt.title('Grayscale Histogram')    #name of the plot
# plt.xlabel('Bins')      #x axis label
# plt.ylabel('No. of pixels')     #y axis label
# plt.plot(gray_histogram)
# plt.xlim([0,256])       #x axis limit
# plt.show()

#color histogram --------------------------

height = img.shape[0]//2
width = img.shape[1]//2

mask = cv.circle(blank, (width, height), 100, (255, 255, 255), -1)

masked = cv.bitwise_and(img, img, mask=mask)
cv.imshow('mask', masked)

plt.figure()    #instantiate
plt.title('Color Histogram')    #name of the plot
plt.xlabel('Bins')      #x axis label
plt.ylabel('No. of pixels')     #y axis label

colors = ('b', 'g', 'r')    #tuple of elements of color
for i, col in enumerate(colors):
    hist = cv.calcHist([img], [i], None, [256], [0, 256])
    plt.plot(hist, color = col)
    plt.xlim([0, 256])
    
plt.show()

cv.waitKey(0)