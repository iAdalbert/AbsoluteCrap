import time
import board
import pwmio
from adafruit_motor import servo
import adafruit_hcsr04

pwm = pwmio.PWMOut(board.GP27, duty_cycle=2 ** 15, frequency=50)
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.GP15, echo_pin=board.GP14)
my_servo = servo.Servo(pwm)

i = 0
while True:
    my_servo.angle = i
    time.sleep(0.1)
    try:
        print((sonar.distance,))
    except RuntimeError:
        print("Retrying!")
    print("kat: " + str(i/2))
    i = i + 2
    if i == 180:
        i = 0