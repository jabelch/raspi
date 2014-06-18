import cwiid
import time
wm = cwiid.Wiimote()

time.sleep(1)

for i in range(16):
  wm.led = i
  wm.rumble = True
  time.sleep(.05)
  wm.rumble = False
  time.sleep(.1) 

wm.rpt_mode = cwiid.RPT_BTN
old_btn = 0
power = 0 #power off

while(True):
  btn = wm.state['buttons']

  if btn == 0:
    old_btn = -1
    time.sleep(.1)
    continue
  elif btn == old_btn: 
    time.sleep(.1)
    continue
  else:
    if btn == 4:
      if power == 0:
        power = 1
      else:
        power = 0
      print 'power = ' + str(power)

    print btn
    old_btn = btn
#    btn = 0
  


