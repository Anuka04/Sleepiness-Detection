# Import the necessary packages 
import datetime as dt
from cacl_ar import *
from imutils import face_utils 
from imutils.video import VideoStream
import matplotlib.pyplot as plt
from matplotlib import style 
import imutils 
import dlib
import argparse 
import cv2 
from playsound import playsound
from scipy.spatial import distance as dist
import numpy as np
import time

style.use('fivethirtyeight')

#all eye  and mouth aspect ratio with time
ear_list=[]
total_ear=[]
mar_list=[]
total_mar=[]
ts=[]
total_ts=[]
# Construct the argument parser and parse the arguments 
ap = argparse.ArgumentParser() 
ap.add_argument("-p", "--shape_predictor", required = True, help = "path to dlib's facial landmark predictor")
ap.add_argument("-r", "--picamera", type = int, default = -1, help = "whether raspberry pi camera shall be used or not")
args = vars(ap.parse_args())

# Constant which will work as the threshold for EAR value, below which it is a blink
EAR_THRESHOLD = 0.3
# Costant to hold the consecutive number of frames to consider for a blink 
CONSECUTIVE_FRAMES = 20 
# Another constant which will work as a threshold for MAR value
MAR_THRESHOLD = 14

# Initialize two counters 
BLINK_COUNT = 0 
FRAME_COUNT = 0 

# Now, intialize the dlib's face detector model and the landmark predictor model
print("Loading predictor.....")
detect = dlib.get_frontal_face_detector() 
predict = dlib.shape_predictor(args["shape_predictor"])

# Grab the indexes of the facial landamarks for the left and right eye respectively 
(lstart, lend) = face_utils.FACIAL_LANDMARKS_IDXS["left_eye"]
(rstart, rend) = face_utils.FACIAL_LANDMARKS_IDXS["right_eye"]
(mstart, mend) = face_utils.FACIAL_LANDMARKS_IDXS["mouth"]

print("Loading Camera.....")
vs = VideoStream(usePiCamera = args["picamera"] > 0).start()

count_sleep = 0
count_yawn = 0 

 
# First, we loop over all the frames and detect the faces
while True: 
	# Extract frame 
	frame = vs.read()
	cv2.putText(frame, "PRESS 'o' TO CLOSE", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 0), 3) 
	# Resize frame 
	frame = imutils.resize(frame, width = 500)
	# Convert the frame to grayscale 
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	# Detect faces 
	rects = detect(frame, 1)

	# Next we loop over all the face detections and apply the predictor 
	for (i, rect) in enumerate(rects): 
		shape = predict(gray, rect)
		# Convert it to a (68, 2) size numpy array 
		shape = face_utils.shape_to_np(shape)

		# Rectangle around detected face 
		(x, y, w, h) = face_utils.rect_to_bb(rect) 
		cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0))	

		leftEye = shape[lstart:lend]
		rightEye = shape[rstart:rend] 
		mouth = shape[mstart:mend]
		# Compute the EAR for both the eyes 
		leftEAR = eye_aspect_ratio(leftEye)
		rightEAR = eye_aspect_ratio(rightEye)
		EAR = (leftEAR + rightEAR) / 2.0		

		ts.append(dt.datetime.now().strftime('%H:%M:%S.%f'))

		leftEyeHull = cv2.convexHull(leftEye)
		rightEyeHull = cv2.convexHull(rightEye)
		# Draw contours for both eyes and mouth
		cv2.drawContours(frame, [leftEyeHull], -1, (124,252,0), 1)
		cv2.drawContours(frame, [rightEyeHull], -1, (124,252,0), 1)
		cv2.drawContours(frame, [mouth], -1, (124,252,0), 1)

		MAR = mouth_aspect_ratio(mouth)
		mar_list.append(MAR/10)
		# If EAR < EAR_THRESHOLD, it indicates that person is blinking
		# Count the number of frames for which the eyes remains closed 
		if EAR < EAR_THRESHOLD: 
			FRAME_COUNT += 1

			cv2.drawContours(frame, [leftEyeHull], -1, (0, 0, 255), 1)
			cv2.drawContours(frame, [rightEyeHull], -1, (0, 0, 255), 1)

			if FRAME_COUNT >= CONSECUTIVE_FRAMES: 
				count_sleep += 1
				playsound('sound files/alarm.mp3')
				cv2.putText(frame, "YOU ARE SLEEPY!", (270, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2)
		else: 
			if FRAME_COUNT >= CONSECUTIVE_FRAMES: 
				playsound('sound files/sleep.mp3')
			FRAME_COUNT = 0

		# Check if the person is yawning
		if MAR > MAR_THRESHOLD:
			count_yawn += 1
			cv2.drawContours(frame, [mouth], -1, (0, 0, 255), 1) 
			cv2.putText(frame, "YOU ARE SLEEPY!", (270, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2)
			playsound('sound files/alarm.mp3')
			playsound('sound files/yawn.mp3')
	cv2.imshow("Output", frame)
	key = cv2.waitKey(1) & 0xFF 
	
	

	if key == ord('o'):
		break

cv2.destroyAllWindows()
vs.stop()
