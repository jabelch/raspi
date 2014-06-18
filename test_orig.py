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

while(True):
  btn = wm.state['buttons']

  if btn == 0 or btn == old_btn: 
    time.sleep(.1)
    continue
  else:
    print btn
    old_btn = btn
   # btn = 0
  


