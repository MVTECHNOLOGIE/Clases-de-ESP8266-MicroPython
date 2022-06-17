from machine import Pin   #importar librerias
import time               

ldr = machine.ADC(0)     #Seleccionamos el pin AO ADC "pin analógico"

while True:               #Se utiliza para especificar un bucle infinito 
    
     valor = ldr.read()        # La variable "valor" es igual al voltaje lee, con una precisión de 10 bits
     print("Valor LDR: " , valor) # Imprimimos las variables, en este caso es "valor
     
     #luz = round(valor/1023*100,3)
     #print("Luz solar: " , luz, "%")  
     
     # Los valores variaran entre "0 y 1024
     
     time.sleep(1)                    #Tiempo de espera
 