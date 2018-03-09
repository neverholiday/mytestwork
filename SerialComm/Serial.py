import serial
import time

Serial = serial.Serial('/dev/ttyACM0',9600)

# TX
stateInput = 0
data = 256

while True :
	data = raw_input("Pim si : ")
	if data != '-1':
		if data != 256:
			Serial.write(data)
			data = 256
			time.sleep(1)
		
		data_recieve = Serial.read()
		print data_recieve
	else:
		Serial.close()
		break

# RX