Install CH340 driver - CH34xVCPDriver

`esptool.py --chip esp32 --port /dev/tty.wchusbserial2140 erase_flash`

`esptool.py --chip esp32 --port /dev/tty.wchusbserial2140 --baud 460800 write_flash -z 0x1000 esp32-20230426-v1.20.0.bin`

Wiring:

Connect GND & PIN 25 via resistor 10K Ohm

Connect rain gauge 1st wire to 3.3V

Connect rain gauge 2nd wire to Pin 25 (together with resistor!)