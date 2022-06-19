from machine import Pin, ADC, PWM     #Importamos librerías   
import time


LED = PWM(Pin(2, Pin.OUT))     # Declaramos el pin 15 como PWM
LED.freq(1000)     # 1000Hz

POT = ADC(0)     #Declaramos la variable para la lectura analógica pin 26


while True: #Bucle infinito
    
  Valor = POT.read()      # Almacenamos los valores leídos de nuestro potenciómetro en la variable "Valor"
                          #que serán de 0 a 1024
  
  #val= round(Valor/1024*100,1)   # redondeamos de 0 a 100
  #print("Porcentaje: ",val, "%") # Imprimimos los valores almacenados en la variable "val"
  
  print(Valor)           # Imprimimos los valores almacenados en la variable "Valor"
  
  LED.duty(Valor)    # Establesemos el valor del ciclo de trabajo como el del valor del potenciómetro
  time.sleep(0.25)   # Le damos un diempo de 250ms