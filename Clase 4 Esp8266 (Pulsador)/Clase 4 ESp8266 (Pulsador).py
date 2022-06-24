#Importamos la librerias.
from machine import Pin
import time

LED = Pin(16,Pin.OUT)   #Declaramos como salida el pin 16 almacenándolo en la variable "LED". 
LED2 = Pin(2,Pin.OUT)  #Declaramos como salida el pin 2 almacenándolo en la variable "LED2".
LED3 = Pin(12,Pin.OUT)  #Declaramos como salida el pin 12 almacenándolo en la variable "LED3".

PULSADOR = Pin(5, Pin.IN,Pin.PULL_UP) #Declaramos como salida el pin 16 almacenándolo en la
                                         #variable "Pulsador" y activando la resistencia interna para Pull-Down.
PULSADOR2 = Pin(4 , Pin.IN) #Declaramos como salida el pin 16 almacenándolo en la variable "Pulsador2".

while True: #Iniciamos bucle infinito
    
    if PULSADOR.value() == 0: #Si el pulso enviado del pulsador1 es alto "High".
        LED.value(1)           #Encendera el LED.
        print("Led Rojo Encendido") #Imprimiendo "Led Rojo Encendido".
        time.sleep(0.2)             #Le damos un tiempo de 200ms para evitar rebote.
    else :                     #Si el pulso no esta en alto "High".
        LED.value(0)           #Entonces se Apagara el LED.
        
    if PULSADOR2.value() == 1:  #Si el pulso enviado del pulsador 2 es alto "High".
        LED3.value(1)           #Encendera el LED.
        print("Led Verde Encendido") #Imprimiendo "Led Rojo Encendido".
        time.sleep(0.2)              #Le damos un tiempo de 200ms para evitar rebote.
    else :                     #Si el pulso no esta en alto "High".
        LED3.value(0)          #Entonces se Encendera el LED.
    
    if PULSADOR2.value() == 1 and PULSADOR.value() == 0:  #Si el pulso enviado del pulsador 2 es alto "High".
        LED2.value(1)           #Encendera el LED.
        print("Led Azul Encendido") #Imprimiendo "Led Rojo Encendido".
        time.sleep(0.2)              #Le damos un tiempo de 200ms para evitar rebote.
    else :                     #Si el pulso no esta en alto "High".
        LED2.value(0)          #Entonces se Encendera el LED.
        