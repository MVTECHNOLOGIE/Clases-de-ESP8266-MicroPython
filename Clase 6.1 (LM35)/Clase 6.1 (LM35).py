from machine  import Pin, ADC
import time

analog_value = ADC(0)
conversion_factor = 3.3/ 1024

while True:
    
    temp_voltage_raw = analog_value.read()
    convert_voltage = temp_voltage_raw*conversion_factor
    tempC = convert_voltage/(10.0 / 1000)
    
    print("Temperature: ",tempC, "°C", sep=" ")
    
    time.sleep(2)