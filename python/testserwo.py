import time
import board
import pwmio
from adafruit_motor import servo
 
# create a PWMOut object on Pin GP27.
pwm = pwmio.PWMOut(board.GP27, duty_cycle=2 ** 15, frequency=50)
 
# Create a servo object, my_servo.
my_servo = servo.Servo(pwm)
i = 0
while True:
    my_servo.angle = i
    time.sleep(0.1)
    print(i)
    i = i + 1
    if i == 180:
        i = 0