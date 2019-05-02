
import time
from adafruit_servokit import ServoKit
import pygame
pygame.init()


pwm = ServoKit(channels=16)
pwm.continuous_servo[0].throttle = 0

gamepad = pygame.joystick.Joystick(0)
gamepad.init()

#Four motors 3 channels
#Verticle motors connected with Y-spliters
verticle = 0
left = 1
right = 2

while(True):
    
    pygame.event.get()

    if  gamepad.get_button(3) == 1:
        pwm.continuous_servo[verticle].throttle = 1

    elif  gamepad.get_button(4) == 1:
        pwm.continuous_servo[verticle].throttle = -1

    else:
        pwm.servo[vericle].angle = 0

    
    pwm.continuous_servo[left].throttle = gamepad.get_axis(1)
    pwm.continuous_servo[right].throttle = gamepad.get_axis(2)

