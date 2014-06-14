import RPi.GPIO as GPIO
import time
import signal
import sys

GPIO.setmode(GPIO.BCM)

#+ is +5Volts VCC
#- is Ground
#a is left relay (as viewed from reading silk screen)
#b is right relay
#+......ab-..-
#.............

A = 23 #a relay is on pin 23
B = 24 #b relay is on pin 24

def togglePin (pin, dir):
  GPIO.setup(pin, dir, pull_up_down=GPIO.PUD_UP)

def main():
  while(True):
    togglePin(B, GPIO.OUT)
    time.sleep(1)  
    togglePin(B, GPIO.IN)
    time.sleep(1)

if __name__ == "__main__":
  try:
    main()
  except:
    togglePin(A, GPIO.IN)
    togglePin(B, GPIO.IN)
