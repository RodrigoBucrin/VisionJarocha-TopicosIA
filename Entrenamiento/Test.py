import cv2
import numpy as np

#ARCHIVO PARA PROBAR MIS HAARC


 
kernel=np.ones((3,3))
cam = cv2.VideoCapture(0)#("http://192.168.0.4:4747/mjpegfeed")


face_csc = cv2.CascadeClassifier('haarcascade/cascade.xml')

def BuscarPersonas():
	BuscarRostros()


def BuscarRostros(): 
		for (x, y, w, h) in faces:						#Obtenemos los puntos para el ROI					
			roi=gray[y:y+h,x:x+w]										#Area de interés
			blur=cv2.GaussianBlur(roi,(3,3),1)						#Desenfoque
			dilate=cv2.dilate(blur, kernel, iterations=5) #7			#Dilatado
			erode=cv2.erode(dilate,kernel,iterations=5)	#7		#Erosión
			canny=cv2.Canny(erode,150,200)
			contours, hierarchy = cv2.findContours(canny,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
			cv2.drawContours(img[y:y+h,x:x+w],contours,-1,(0,255,0),3)
		#cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 5)
		#Imprimir el texto
			cv2.putText(img, "Rostro detectado", (x+w+ 20, y + 20), cv2.FONT_HERSHEY_COMPLEX, .7,(0,255, 0), 2)
			if faces is ():
				print("No veo rostros")

while(True):
	ret, img = cam.read()
	
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	faces = face_csc.detectMultiScale(img, 1.4,3)
	
	
	BuscarPersonas()

	cv2.imshow('img', img)
	#cv2.imshow('cuerpos',roi)

	key = cv2.waitKey(1)
	if key == 27:
		break

#cam.release()
cv2.destroyAllWindows()

