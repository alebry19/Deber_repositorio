import cv2
import sys
#import conexion
import time
from tkinter import ttk
from tkinter import *
from PIL import Image, ImageTk
import numpy as np #Librería para la creación de arrays


def hora():
        return str("Fecha actual: ") +str(time.localtime()[2]) + "-"+str(time.localtime()[1])+"-"+str(time.localtime()[0])+"\n"+ str ("Hora: ") + str (time.localtime()[3])+":"+str(time.localtime()[4])+":"+str(time.localtime()[5])
def refresh_fecha():
        root.after(1000,refresh_fecha)
        mifecha.set(hora())
        hora2.config(text=hora())


def hsv(int): #funcion para controlar el valor de los sliders
    hMin.set(slider.get())
    hMax.set(slider1.get())
    sMin.set(slider2.get())
    sMax.set(slider3.get())  
    vMin.set(slider4.get())
    vMax.set(slider5.get())    


def onClossing(): #función para el cierre
    print ("lower= np.array(["+str(hMin.get())+","+str(sMin.get())+","+str(vMin.get())+"])")
    print ("upper= np.array(["+str(hMax.get())+","+str(sMax.get())+","+str(vMax.get())+"])")

    root.quit()
    cap.release()
    print("Camara desconectada")
    root.destroy()


def callback():
     
    ret, frame = cap.read() #Captura del frame

    if ret:

         ######PROCESAMIENTO DE LA IMAGEN###########

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) #Transformación a escalas grises dentro de una variable

        #Arrays para controlar los métodos de los sliders
        lower= np.array([hMin.get(), sMin.get(), vMin.get()]) 
        upper= np.array([hMax.get(), sMax.get(), vMax.get()])

        #Creacion de la mascara de color para detectar valores y colores
        mask = cv2.inRange(hsv, lower, upper)

        kernel = np.ones((10,10),np.uint8) #Creación de un kernel (matriz de 1's)
        opening = cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel)
        close = cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernel)


        ######SEGMENTACION#####
        #Para la detección de contornos
        contornos,_ = cv2.findContours(opening.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        print (len(contornos))

        #For para recorrer todos los contornos
        for cnt in contornos:
             
            cv2.drawContours(frame, [cnt], 0, (0,255,0),3)

        

        #t, binario = cv2.threshold(hsv, valorUmbral.get(), 255, cv2.THRESH_BINARY_INV) #Asignación de las escalas que se deseen 

          
        img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) #Transformación del espectro de color (BGR a RGB)
        img = Image.fromarray(img) #transformamos en un array
        tkimage = ImageTk.PhotoImage(img) #Creamos una imagen de tipo tkinter
        label.configure(image = tkimage) #Configurar el label como tkimage
        label.image = tkimage #Se agrega la imagen creada al label


        img1 = mask #Transformación del espectro de color (tomando la variable)
        img1 = Image.fromarray(img1) #transformamos en un array
        tkimage1 = ImageTk.PhotoImage(img1) #Creamos una imagen de tipo tkinter
        label1.configure(image = tkimage1) #Configurar el label como tkimage
        label1.image = tkimage1 #Se agrega la imagen creada al label

    else:
          onClossing() #Llamamos a la función onClossing para cerrar la ventana

    root.after(10,callback)
          

def salir():
        root.destroy()


# Método para conectar la bdd invernadero-final con el código AI
#def conectar():
#        conexion.conecxion()
#        conexion.conecxion().mostrar()
     
cap = cv2.VideoCapture(0)

if cap.isOpened():
     print("Camara inicializada")
else:
     sys.exit("Camara desconectada")

root = Tk() #Objeto para llamar a Tkinter
root.protocol("WM_DELETE_WINDOW",onClossing) #Protocolo para asignar la opción de cierre
root.title("Visión Artificial-Módulo de Cosecha")
root.config(bg="#084d6e")
titulo= Label(text="SISTEMA",font=("Arial",15))
titulo.grid(row=0,column=0,sticky='e')
titulo= Label(text=" DE COSECHA ",font=("Arial",15))
titulo.grid(row=0,column=1,sticky='w')
label  = Label(root) #Etiqueta para ingresar una imagen

mifecha=StringVar()
hora1= Label(textvar=mifecha,font=("Arial",16))
hora2= Label(text=" ",font=("Arial",16))
hora2.grid(row=1, column=0)
hora1.grid(row=1, column=1)



label.grid(row=2,column=0)

label1  = Label(root) #Etiqueta para ingresar otra imagen
label1.grid(row=2,column=1)

#Los sliders son las barras desplazadoras con los valores que asignemos

slider = Scale(root, label = "Hue Min", from_= 0, to = 255, orient = HORIZONTAL, 
command=hsv, length= 400)
slider.grid(row=3,column=0)

slider1 = Scale(root, label = "Hue Max", from_= 0, to = 255, orient = HORIZONTAL, 
command=hsv, length= 400)
slider1.grid(row=3,column=1)

slider2 = Scale(root, label = "Saturación Min", from_= 0, to = 255, orient = HORIZONTAL, 
command=hsv, length= 400)
slider2.grid(row=4,column=0)

slider3 = Scale(root, label = "Saturación Max", from_= 0, to = 255, orient = HORIZONTAL, 
command=hsv, length= 400)
slider3.grid(row=4,column=1)

slider4 = Scale(root, label = "Value Min", from_= 0, to = 255, orient = HORIZONTAL, 
command=hsv, length= 400)
slider4.grid(row=5,column=0)

slider5 = Scale(root, label = "Value Max", from_= 0, to = 255, orient = HORIZONTAL, 
command=hsv, length= 400)
slider5.grid(row=5,column=1)


mensaje= Label(text="                                          ROSA LISTA PARA LA COSECHA                                            ",font=("Arial",15))
mensaje.grid(row=6,column=0)
mensaje.config(bg="#e0de05")


boton_salida=ttk.Button(text="SALIR")
boton_salida.grid(row=7,column=1, sticky='e')


slider.set(166)
slider1.set(255)
slider2.set(150)
slider3.set(255)
slider4.set(71)
slider5.set(255)

hMin = IntVar()
hMax = IntVar()
sMin = IntVar()
sMax = IntVar()
vMin = IntVar()
vMax = IntVar()
boton_salida['command']=salir

valorUmbral = IntVar()
refresh_fecha()
root.after(10,callback) #Llamado a una funcion cada determinado tiempo en 10 seg
#conectar()
root.mainloop() #Ejecución de la ventana