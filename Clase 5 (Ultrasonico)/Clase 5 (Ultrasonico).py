from machine  import Pin
import hcsr04
import time

ultrasonico = hcsr04.HCSR04(trigger_pin=12, echo_pin=14, echo_timeout_us=1000000)

led = Pin (16 ,Pin.OUT)
led2 = Pin (2 ,Pin.OUT)
led2.value(0)

while True:
    
    distancia = ultrasonico.distance_cm()
    
    print('Distancia:', distancia, 'cm')
    
    if distancia <= 10:
        led.off()
    else:
        led.on()

    time.sleep(1)