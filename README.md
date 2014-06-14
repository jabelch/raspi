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

Check that bluetooth is running:
- service bluetooth status

If not, start it:
- /etc/init.d/bluetooth start

Verify address of bluetooth dongle:
- hcitool dev

For more wiimote goodness:
- http://www.brianhensley.net/2012/08/wii-controller-raspberry-pi-python.html
