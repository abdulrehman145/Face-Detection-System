import cv2



face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

video_capture=cv2.VideoCapture(0)

while True:
    ret, frame=video_capture.read()
    if not ret:
        print("failed to grab the camera")

    gray_frame=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    f=face_cascade.detectMultiScale(gray_frame, 1.3,6)
    for (x1,y1,w1,h1) in f:
        cv2.rectangle(frame, (x1,y1), (x1+w1,y1+h1),(255,0,0))

    cv2.imshow("img",frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()


