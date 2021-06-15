
import cv2

#clasificador de Haar:
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')

img = cv2.imread('the-beatles.jpg')
img_gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Busqueda de caras:
faces = faceCascade.detectMultiScale(img_gris, 1.3, 1)

#Recorriendo arreglo 'coordenadas_cara' y dibuja rectangulos sobre la fotografía:
print ("Found {0} faces!".format(len(faces)))
for (x,y,ancho, alto) in faces:
    cv2.rectangle(img, (x,y), (x+ancho, y+alto), (0,255,0) ,2)

#ventana para la salida:
cv2.imshow('Output', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
