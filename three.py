import subprocess
from gpiozero import DistanceSensor,MotionSensor,PingServer
from gpiozero.tools import negated
from signal import pause


arda=PingServer('192.168.1.37')#android
me=PingServer('192.168.1.34')#iphone
mom=PingServer('192.168.1.36')#android

if(arda.value and mom.value and not(me.value)):

	pir = MotionSensor(4)
	dis = DistanceSensor(20,21)
	def calculatedist():
		print('Hareket eden cisim', dis.distance,'m uzaklıkta')
		dis.wait_for_in_range(10000)
	#	subprocess.call("./izle.sh")	
	
	pir.when_motion=calculatedist

pause()
