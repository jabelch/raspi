import RPi.GPIO as GPIO
import signal
import sys
import cwiid
import time

BTN_MINUS = 16 #Minus button
BTN_B = 4 #Wiimote button B

A = 23 #a relay is on pin 23
B = 24 #b relay is on pin 24

def togglePin (pin, in_out):
    dir = GPIO.OUT if in_out else GPIO.IN #Out turns relay on 
    GPIO.setup(pin, dir, pull_up_down=GPIO.PUD_UP)

def wiiWait():
    while(True):
	try:
	    wm = cwiid.Wiimote()
	    print("Found Wiimote!")
	    return wm    
	except:
	    pass

def main():
    wm = wiiWait()

    time.sleep(1)

    for i in range(16):
      wm.led = i
      wm.rumble = True
      time.sleep(.05)
      wm.rumble = False
      time.sleep(.1)
    wm.rpt_mode = cwiid.RPT_BTN
    old_btn = 0
    power = False #power off

    while(True):
      btn = wm.state['buttons']
      if btn == 0:
        old_btn = -1
        time.sleep(.01)
        continue
      elif btn == old_btn:
        time.sleep(.01)
        continue
      else:
        if (btn & BTN_B) == BTN_B:
          power = not power #toggle the power (True->False, False->True)
          togglePin(B, power)
          print 'power = ' + str(power)
#	elif (btn & BTN_MINUS) == BTN_MINUS:
#	  exit(wm)	  
#	  main()
#	  return
        print btn
        old_btn = btn

if __name__ == "__main__":
  try:
    GPIO.setmode(GPIO.BCM)
    main()
  except:
    togglePin(A, False)
    togglePin(B, False)
