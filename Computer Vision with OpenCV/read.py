import cv2 as cv

# image showing tool code ------

def rescaleFrame(frame, scale = 0.2):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation= cv.INTER_AREA)


img = cv.imread('Photos/cat.jpg')
resized_image = rescaleFrame(img)
cv.imshow('cat', resized_image)


    

#cv.waitKey(0)

# video showing tool code ------

capture = cv.VideoCapture('Videos/dog.mp4')

while True:
    isTrue, frame = capture.read()

    frame_resize = rescaleFrame(frame)

    # cv.imshow('Video', frame)
    cv.imshow('video resized', frame_resize)

    if cv.waitKey(20) & 0xFF == ord('d'):
       break
    
capture.release()
cv.destroyAllWindows()

cv.waitKey(0)