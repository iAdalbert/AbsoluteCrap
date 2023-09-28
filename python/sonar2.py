import time
import math
import board
import pwmio
from adafruit_motor import servo
import adafruit_hcsr04

f = open(, "x")
pwm = pwmio.PWMOut(board.GP27, duty_cycle=2 ** 15, frequency=50)
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.GP15, echo_pin=board.GP14)
my_servo = servo.Servo(pwm)
i = 0

while True:
    my_servo.angle = i
    try:
        print(sonar.distance)
        if i < 90:
            beta = i/2
            x = sonar.distance * math.cos(beta)
            y = sonar.distance * math.sin(beta)
                
            print("x= " + str(x) + " y = " + str(y))
    except RuntimeError:
        print("Out of range/error")
    print("kat: " + str(i/2))
    i = i + 2
    if i == 180:
        i = 0
    time.sleep(2)
    