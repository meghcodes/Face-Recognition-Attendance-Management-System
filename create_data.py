#creating database
import cv2, sys, numpy, os
import urlib
import numpy as np
haar_file = 'haarcascade_frontalface_default.xml'
datasets = 'datasets'  #All the faces data will be present this folder
sub_data = 'Gowtham'
####sub_data = 'hai'  #These are sub data sets of folder, for my faces I've used my name

path = os.path.join(datasets, sub_data)
if not os.path.isdir(path):
    os.mkdir(path)
(width, height) = (130, 100)    # defining the size of images 


face_cascade = cv2.CascadeClassifier(haar_file)
##webcam = cv2.VideoCapture(0) #'0' is use for my webcam, if you've any other camera attached use '1' like this
url="http://10.7.81.89:8080/shot.jpg"
# The program loops until it has 30 images of the face.
count = 1
while count < 31: 
##    (_, im) = webcam.read()
    imgPath=urlib.urlopen(url)
    imgNp=np.array(bytearray(imgPath.read()),dtype=np.uint8)
    im=cv2.imdecode(imgNp,-1)
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(im, 1.3, 4)
    for (x,y,w,h) in faces:
        cv2.rectangle(im,(x,y),(x+w,y+h),(255,0,0),2)
        face = gray[y:y + h, x:x + w]
        face_resize = cv2.resize(face, (width, height))
        cv2.imwrite('%s/%s.png' % (path,count), face_resize)
    count += 1
	
    cv2.imshow('OpenCV', im)
    key = cv2.waitKey(10)
    if key == 27:
        break
