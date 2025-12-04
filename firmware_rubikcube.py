#!/usr/bin/env python3
#-- coding: utf-8 --
# import RPi.GPIO as GPIO
import time
import re

def stringParser(movement_string: str):
    """
    Finds matches that fit in pattern <__STRING_PATTERN>
    and returns a list with them, ordered by first to appear.
    """

    __STRING_PATTERN = r"[LRUDBF]['2]?"  

    return re.findall(__STRING_PATTERN, movement_string)




#Set function to calculate percent from angle
def angle_to_percent (angle) :
    if angle > 180 or angle < 0 :
        return False

    start = 4

    end = 12.5
    ratio = (end - start)/180 #Calcul ratio from angle to percent

    angle_as_percent = angle * ratio

    return start + angle_as_percent

def mapPerformRotation(movement_string):
    
    



    return


# def movement_LEFT():

def movement_DOWN():
    
    

    

    pass


def main():

    string = "L'D2URF2B'LL"

    print(stringParser(string))

    exit(0)




    #
    # GPIO.setmode(GPIO.BOARD) #Use Board numerotation mode
    # GPIO.setwarnings(False) #Disable warnings
    #
    # #Use pin 12 for PWM signal
    # pwm_gpio = 12
    # frequence = 50
    # GPIO.setup(pwm_gpio, GPIO.OUT)
    # pwm = GPIO.PWM(pwm_gpio, frequence)
    #
    # #Init at 0°
    # pwm.start(angle_to_percent(0))
    # time.sleep(1)
    #
    # #Go at 90°
    # pwm.ChangeDutyCycle(angle_to_percent(90))
    # time.sleep(1)
    #
    # #Finish at 180°
    # pwm.ChangeDutyCycle(angle_to_percent(180))
    # time.sleep(1)
    #
    # #Close GPIO & cleanup
    # pwm.stop()
    # GPIO.cleanup()

    return

if __name__ == "__main__":
    main()


