import cv2
import imutils
import argparse
import numpy as np  
cap = cv2.VideoCapture(0)
ap = argparse.ArgumentParser()
#ap.add_argument("-i", "--image", required=True,help="path to the input image")
args = vars(ap.parse_args())
while(1):        
    _, frame = cap.read()  
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) 
    lower_red = np.array([110,50,50]) 
    upper_red = np.array([130,255,255]) 
  

    mask = cv2.inRange(hsv, lower_red, upper_red) 
  

    res = cv2.bitwise_and(frame,frame, mask= mask) 
    cv2.imshow('frame',frame) 
    cv2.imshow('mask',mask) 
    cv2.imshow('res',res)

    image = cv2.imread(args["mask"])
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)[1]

    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if imutils.is_cv2() else cnts[1]

    #for c in cnts:
    M = cv2.moments(c)
    cX = int(M["m10"] / M["m00"])
    cY = int(M["m01"] / M["m00"])
    '''
        cv2.drawContours(image, [c], -1, (0, 255, 0), 2)
        cv2.circle(image, (cX, cY), 7, (255, 255, 255), -1)
        cv2.putText(image, "center", (cX - 20, cY - 20),
	cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
        cv2.imshow("Image", image)
    '''
  
    k = cv2.waitKey(5) & 0xFF
    if k == 27: 
        break


cv2.destroyAllWindows() 
cap.release() 


