# Face Detection Using OpenCV
Face Detection Using OpenCV is a real-time Python application that detects human faces from webcam feed using Haar Cascade Classifier. It draws bounding boxes around detected faces and displays the total number of faces in each frame.

**Features**

	-* Real-time face detection from webcam
	-* Uses Haar Cascade for frontal face detection
	-* Bounding boxes drawn around each face
	-* Face count displayed on screen
	-* Option to save frames with detected faces

**Technologies Used**

	-* Python
	-* OpenCV (cv2)
	-* Haarcascade Classifier

**Requirements**

Install the required library:

	pip install opencv-python

Also make sure you have the following file downloaded:

	haarcascade_frontalface_default.xml

**Run the App**

	python face_detection.py

**Future Improvements**

	-* Switch to DNN-based detection for better accuracy
	-* Add age and gender prediction
	-* Add support for video files instead of webcam only
	-* Integrate face recognition module
