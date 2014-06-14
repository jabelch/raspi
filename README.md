raspi
=====

Raspberry Pi Projects

Install minimal raspbian image:
- http://sourceforge.net/projects/minibian/files/

Run:
- apt-get update
- apt-get upgrade
- apt-get install python-dev
- apt-get install python-rpi.gpio
- apt-get install python-cwiid
- apt-get install bluetooth

Bluetooth commands:
- service bluetooth status
- /etc/init.d/bluetooth start
- hcitool dev

For more wiimote goodness:
- http://www.brianhensley.net/2012/08/wii-controller-raspberry-pi-python.html

For more GPIO goodness:
- http://makezine.com/projects/tutorial-raspberry-pi-gpio-pins-and-python/
