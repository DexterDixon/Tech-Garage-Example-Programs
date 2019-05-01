#Created by: Dexter Dixon
#Raspberry Pi Motor Control with Camera

from __future__ import division
import time
import pygame
import Adafruit_PCA9685
import cv2
import numpy as np

pygame.init()

pwm = Adafruit_PCA9685.PCA9685()

#Set variables for motor values
motor_1 = 0
motor_2 = 0
motor_3 = 0

cv2.namedWindow("Vission")

camera1 = cv2.VideoCapture(0)

#Set resolution of the camera
camera1.set(3,480);
camera1.set(4,320);

pwm.set_pwm_freq(60)

print('Initialized')


gamepad = pygame.joystick.Joystick(0)
gamepad.init()


while True:

        pygame.event.get()

        # Capture frame-by-frame
        ret, frame = camera1.read()


        #Display the resulting frame
        cv2.imshow('Vission',frame)

        #Define gamepad axis and button values
        leftstick = gamepad.get_axis(1)
        rightstick = gamepad.get_axis(3)
        button_1 = gamepad.get_button(5)
        button_2 = gamepad.get_button(4)


        motor_1 = (185  * -leftstick + 390)
        motor_2 = (185 * rightstick +390)

        #Forward
        if button_1 == 1:
                motor_3 = 575

        #Bakwards
        elif button_2 == 1:
                motor_3 = -575

        #Stop
        else:
                motor_3 = 0

        #Sends pwm signals to motors
        pwm.set_pwm(0, 0, int(motor_1))
        pwm.set_pwm(1,0, int(motor_2))
        pwm.set_pwm(2, 0, int(motor_3))
        print("Motor_3: ", motor_3)

        key = cv2.waitKey(20)
        if key == 27: # exit on ESC
            break
cv2.destroyWindow("Vission")
vc.release()


