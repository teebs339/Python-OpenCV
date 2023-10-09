import cv2 as cv

def rescaleFrame(frame, scale = 0.6):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation= cv.INTER_AREA)

f_img = cv.imread('Photos/whamen.jpg')
img = rescaleFrame(f_img)
cv.imshow('tea', img)

# we should grayscale the image first
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

# reading the haar .xml file

haar_cascade = cv.CascadeClassifier('haar_face.xml')

faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=4)

print(f'Number of faces found = {len(faces_rect)}')

for(x, y, w, h) in faces_rect:
    cv.rectangle(img, (x,y), (x+w, y+h), (0, 255, 0), thickness=2)

cv.imshow('detected faces', img)

cv.waitKey(0)