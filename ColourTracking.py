# Import library
import cv2
import numpy as np


def nothing(x):
    pass

#create window trackbar HSV
cv2.namedWindow('Trackbar')
cv2.resizeWindow('Trackbar', 600, 300)
cv2.createTrackbar('HueMin', 'Trackbar', 0, 255, nothing)
cv2.createTrackbar('HueMax', 'Trackbar', 0, 255, nothing)
cv2.createTrackbar('SatMin', 'Trackbar', 0, 255, nothing)
cv2.createTrackbar('SatMax', 'Trackbar', 0, 255, nothing)
cv2.createTrackbar('ValMin', 'Trackbar', 0, 255, nothing)
cv2.createTrackbar('ValMax', 'Trackbar', 0, 255, nothing)



# code for using camera
webcam_video = cv2.VideoCapture(0)

#create window untuk coding
while True:
    # code mamulai Webcam
    success, video = webcam_video.read()

    # mengubah BGR image ke format HSV
    img = cv2.cvtColor(video, cv2.COLOR_BGR2HSV)
    hmin = cv2.getTrackbarPos('HueMin', 'Trackbar')
    hmax = cv2.getTrackbarPos('HueMax', 'Trackbar')
    smin = cv2.getTrackbarPos('SatMin', 'Trackbar')
    smax = cv2.getTrackbarPos('SatMax', 'Trackbar')
    vmin = cv2.getTrackbarPos('ValMin', 'Trackbar')
    vmax = cv2.getTrackbarPos('ValMax', 'Trackbar')
    print(hmin, hmax, smin, smax, vmin, vmax)

    lower = np.array([hmin, smin, vmin])
    upper = np.array([hmax, smax, vmax])
    #code untuk hasil dari atau setelah dari trackbar HSV
    mask = cv2.inRange(img, lower, upper)

    mask_contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)  # Finding contours in mask image
    # menemukan track kontur
    if len(mask_contours) != 0:
        for mask_contour in mask_contours:
            if cv2.contourArea(mask_contour) > 500:
                x, y, w, h = cv2.boundingRect(mask_contour)

                #frame Object traking
                cv2.rectangle(mask, (x, y), (x + w, y + h), (70, 255, 255), 3) #drawing rectangle

                #menentukan titik tengah object
                tengah = cv2.moments(mask)
                x = int (tengah["m10"]/tengah["m00"])
                y = int (tengah["m01"]/tengah["m00"])

                #object penanda tengah
                cv2.circle(mask, (x,y), 3, (34, 255, 140),3)

    cv2.imshow("mask vidio",mask)  # tampilan mask vidio0
    cv2.imshow("window", video)  # tampilkan hasil WebCam
    cv2.waitKey(1)