import cv2
from directkeys import PressKey, ReleaseKey, W, A, S, D, ENTER , Q , SPACE


puños_csc=cv2.CascadeClassifier('haarcascade/closed_palm.xml')
caras_csc= cv2.CascadeClassifier('haarcascade/frontalface.xml')
ojos_csc= cv2.CascadeClassifier('haarcascade/smile.xml')

# Para implementar en Fase 2
#orb = cv2.ORB_create(nfeatures=1700)

cap=cv2.VideoCapture(0)


lec1=True
#600,300
#480,220

while True:
    ret,img=cap.read()
    img = cv2.resize(img, (600, 480))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    caras = caras_csc.detectMultiScale(gray, 1.3, 3)

    for (x, y, w, h) in caras:
        img=cv2.rectangle(img, (x, y+20), (x + w, y + h), (0, 255, 255), 2)
        roi_face = gray[y:y+h,x:x+w]
        roi_face_clr = img[y:y+h,x:x+w]      
        ojos = ojos_csc.detectMultiScale(roi_face_clr, 1.3, 50)
        ReleaseKey(Q)
        for (x, y, w, h) in ojos:
                cv2.rectangle(img, (x, y+20), (x + w, y + h), (0, 255, 255), 2)
                if(len(ojos)>=1):
                    cv2.putText(img, "Sonriendo", (70,70), cv2.FONT_HERSHEY_PLAIN, 3,(0,255,0),2)
                    PressKey(Q)
                if(len(ojos)<=0):
                    ReleaseKey(Q)
        
        
        
        
        if ((x+w/2) > 0 and (x+w/2) < 200):
            label = "Izquierda"
            cv2.putText(img, label, (x, y+40), cv2.FONT_HERSHEY_COMPLEX, .7, (0, 255, 0), 1)
            ReleaseKey(W)
            ReleaseKey(ENTER)
            PressKey(A)



            # print("Izquierda")

        if ((x+w/2) > 200 and (x+w/2) < 400):
            puños = puños_csc.detectMultiScale(gray, 1.1, 2)
            label = "Centro"
            cv2.putText(img, label, (x, y+40), cv2.FONT_HERSHEY_COMPLEX, .7, (0, 255, 0), 1)
            ReleaseKey(S)
            ReleaseKey(D)
            ReleaseKey(A)
            PressKey(W)
            
            
           
            
            
            
            
            
            
            if len(puños)==1:
                for (x, y, w, h) in puños:
                    label = "ENTER"
                    cv2.putText(img, label, (x, y + 40), cv2.FONT_HERSHEY_COMPLEX, .7, (0, 255, 0), 1)
                    ReleaseKey(W)
                    ReleaseKey(SPACE)
                    PressKey(ENTER)           

           #ReleaseKey(D)
           #ReleaseKey(A)
          # PressKey(W)



           # print("Centro")

        if ((x+w/2) > 400 and (x+w/2) < 600):
            label = "Derecha"
            cv2.putText(img, label, (x, y+40), cv2.FONT_HERSHEY_COMPLEX, .7, (0, 255, 0), 1)
            ReleaseKey(W)
            ReleaseKey(ENTER)
            #PressKey(D)
            PressKey(D)

           #print("Derecha")


    cv2.rectangle(img,(0,0),(200,480),(0,255,0),1)# (0,200]
    label = "Izquierda"
    cv2.putText(img, label, (80, 20), cv2.FONT_HERSHEY_COMPLEX, .4, (0, 255, 0), 1)

    cv2.rectangle(img, (200,0 ), (400, 480), (0, 255, 0), 1)  #[200,400]
    label = "Centro"
    cv2.putText(img, label, (280, 20), cv2.FONT_HERSHEY_COMPLEX, .4, (0, 255, 0), 1)

    cv2.rectangle(img, (400, 0), (599, 480), (0, 255, 0), 1) #[400,600)
    label = "Derecha"
    cv2.putText(img, label, (480, 20), cv2.FONT_HERSHEY_COMPLEX, .4, (0, 255, 0), 1)





    cv2.imshow("Vision Jarocha",img)
    #cv2.imshow("Caras",thresh)
    #cv2.imshow("Hola2", gray)
    if cv2.waitKey(25) == ord('e'):
        break

cap.release()
cv2.destroyAllWindows()
