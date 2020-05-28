from gpiozero import PingServer, LEDBoard
from gpiozero.tools import negated
from signal import pause

status = LEDBoard(
    arda=LEDBoard(red=14, green=15),
    me=LEDBoard(red=17, green=18)
)

statuses = {
    PingServer('192.168.1.37'): status.arda,
    PingServer('192.168.1.39'): status.me,
}

for server, leds in statuses.items():
    leds.green.source = server
    leds.green.source_delay = 60
    leds.red.source = negated(leds.green)
    if (leds.green):
       print("home")
pause()
