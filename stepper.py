import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

coil_A_1_pin = 11
coil_A_2_pin = 13
coil_B_1_pin = 15
coil_B_2_pin = 31

GPIO.setup(coil_A_1_pin, GPIO.OUT)
GPIO.setup(coil_A_2_pin, GPIO.OUT)
GPIO.setup(coil_B_1_pin, GPIO.OUT)
GPIO.setup(coil_B_2_pin, GPIO.OUT)

def forward(delay, steps):
 for i in range(0, steps):
	 setStep(1, 0, 1, 0)
	 time.sleep(delay)
	 setStep(0, 1, 1, 0)
	 time.sleep(delay)
	 setStep(0, 1, 0, 1)
	 time.sleep(delay)
	 setStep(1, 0, 0, 1)
	 time.sleep(delay) 
def backwards(delay, steps):
 for i in range(0, steps):
	 setStep(1, 0, 0, 1)
	 time.sleep(delay)
	 setStep(0, 1, 0, 1)
	 time.sleep(delay)
	 setStep(0, 1, 1, 0)
	 time.sleep(delay)
	 setStep(1, 0, 1, 0)
	 time.sleep(delay) 
def setStep(w1, w2, w3, w4):
 GPIO.output(coil_A_1_pin, w1)
 GPIO.output(coil_A_2_pin, w2)
 GPIO.output(coil_B_1_pin, w3)
 GPIO.output(coil_B_2_pin, w4)
while True:
 delay = int(input('Adim arasi bekleme suresi (milisaniye)?'))
 steps = int(input('Ileri kac adim?'))
 forward((delay) / 1000.0, (steps))
 steps = int(input('Geri kac adim? '))
 backwards((delay) / 1000.0, (steps))
