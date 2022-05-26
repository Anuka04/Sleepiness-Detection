# Define the function for calculating the Eye Aspect Ratio(EAR)
from scipy.spatial import distance as dist 
def eye_aspect_ratio(eye):
	# Vertical eye points
	d1 = dist.euclidean(eye[1], eye[5])
	d2 = dist.euclidean(eye[2], eye[4])
	# Horizontal eye points
	d3 = dist.euclidean(eye[0], eye[3])

	# The EAR Equation 
	EAR = (d1 + d2) / (2.0 * d3)
	return EAR

def mouth_aspect_ratio(mouth): 
	d1 = dist.euclidean(mouth[13], mouth[19])
	d2 = dist.euclidean(mouth[14], mouth[18])
	d3 = dist.euclidean(mouth[15], mouth[17])

	MAR = (d1 + d2 + d3) / 3.0
	return MAR