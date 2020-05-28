from gpiozero import PingServer
from signal import pause
mom = PingServer('192.168.1.36')
me = PingServer('192.168.1.34')
arda = PingServer('192.168.1.37')

print('Arda:',arda.value)
print('Mom:',mom.value)
print('Me:',me.value)

