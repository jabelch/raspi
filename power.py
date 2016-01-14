import RPi.GPIO as GPIO

genDetectPin = 17
invDetectPin = 18
cbDetectPin = 27

buttonPin = 25

genOnPin = 23
genOffPin = 24
genAutoPin = 22

GPIO.setmode(GPIO.BCM)
GPIO.setup(genDetectPin, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(invDetectPin, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(cbDetectPin, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

GPIO.setup(buttonPin, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(genOnPin, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(genOffPin, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(genAutoPin, GPIO.IN, pull_up_down = GPIO.PUD_UP)


def genOutput(self):
  print("Generator Powered")

def invOutput(self):
  print("Inverter Powered")

def cbOutput(self):
  print("Circuit Breaker Powered")

def pressGeneratorButton(relayPin):
  GPIO.setup(relayPin, GPIO.OUT)

def releaseGeneratorButton(relayPin):
  GPIO.setup(relayPin, GPIO.IN)

GPIO.add_event_detect(genDetectPin, GPIO.RISING, callback=genOutput, bouncetime=300)
GPIO.add_event_detect(invDetectPin, GPIO.RISING, callback=invOutput, bouncetime=300)
GPIO.add_event_detect(cbDetectPin, GPIO.RISING, callback=cbOutput, bouncetime=300)

#GPIO.add_event_detect(buttonPin, GPIO.RISING, callback=pressGeneratorButton, bouncetime=300) 
#GPIO.add_event_detect(buttonPin, GPIO.FALLING, callback=releaseGeneratorButton, bouncetime=300) 

count=0
while count < 30:
  if count % 3 == 0:
    b=genOffPin
  elif count % 3 == 1:
    b=genOnPin
  elif count % 3 == 2:
    b=genAutoPin
  GPIO.wait_for_edge(buttonPin, GPIO.FALLING, bouncetime=100)
  pressGeneratorButton(b)
  print("Button Pressed")
  GPIO.wait_for_edge(buttonPin, GPIO.RISING, bouncetime=100)
  releaseGeneratorButton(b)
  print("Button Released")
  count += 1
  
GPIO.cleanup()
