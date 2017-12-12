import cv2
import numpy as np

faceDetect =  cv2.CascadeClassifier('haarcascade_frontalface_default.xml');
cam = cv2.VideoCapture(0);

rec = cv2.face.LBPHFaceRecognizer_create();
rec.read("recognizer\\trainingData.yml")
id = 0
fontface = cv2.FONT_HERSHEY_COMPLEX_SMALL
fontscale = 1.5
fontcolor = (0,0,255)

while(True):
    ret, img=cam.read();
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceDetect.detectMultiScale(gray,1.3,5);
    for(x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)
        id, conf = rec.predict(gray[y:y+h, x:x+w])
        if(id==1): id= "billy_SAD FACE"
        elif(id==2): id="billy_HAPPY FACE"
        elif(id==3): id= "RISHABH" 
        elif(id==4): id="RAMIN"
        cv2.putText(img, str(id), (x,y+h), fontface, fontscale, fontcolor);
    cv2.imshow("Face", img)
    if(cv2.waitKey(1) == ord('q')):
        break;
    
cam.release()
cv2.destroyAllWindows()
