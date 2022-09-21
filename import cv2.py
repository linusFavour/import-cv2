import cv2
video = cv2.VideoCapture(0)
frontal_face = cv2.CascadeClassifier(r"C://Users//pc//Desktop//vsprojects//frontalface.xml")

while True:
    ret,frame = video.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = frontal_face.detectMultiScale(gray)
    for(x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),5)
    cv2.imshow("frame_name",frame)
    if cv2.waitKey(20) and 0xFF==ord('q'):
        break
    
    
    
    
video.release()
cv2.destroyAllWindows()
