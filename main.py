import cv2
from mtcnn.mtcnn import MTCNN
detector = MTCNN()
def IITFaceDetection_CountingTrigger(image,count):
	if count > 2:
		image=cv2.putText(image, "TRIGGER MET", (100,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 3, cv2.LINE_AA) 
	else:
		pass
	return image
def IITFaceDetection():
	ip_address= "rtp://192.168.18.134:8555"
	#We can use IP of a webcam to take video stream from
	videoall = cv2.VideoCapture(ip_address)
	while videoall.isOpened(): 
		#Capture frame-by-frame
		__, image = videoall.read()
		count=0
		#Using MTCNN to detect faces
		result = detector.detect_faces(image)
		if result != []:
			count=len(result)

			cv2.putText(image, str(count), (50,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,155,255), 2, cv2.LINE_AA) 
			#Trigger
			image=IITFaceDetection_CountingTrigger(image, int(count))
			for person in result:
				bounding_box = person['box']
				
		
				cv2.rectangle(image,
							  (bounding_box[0], bounding_box[1]),
							  (bounding_box[0]+bounding_box[2], bounding_box[1] + bounding_box[3]),
							  (0,155,255),
							  2)
		
		#display resulting frame
		cv2.imshow('Face Detection App IITD',image)
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
	#When everything's done, release capture
	videoall.release()
	cv2.destroyAllWindows()

if __name__=="__main__":
	IITFaceDetection()
