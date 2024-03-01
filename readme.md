### Dependencies:
- CH340 driver - CH34xVCPDriver
- make 
- esptool.py 
- ampy

### Installation on ESP32
Modify main.py picking proper instance, and then:
```bash
cd scripts/
make
```

### Wiring:

Connect GND & PIN 25 via resistor 10K Ohm

Connect rain gauge 1st wire to 3.3V

Connect rain gauge 2nd wire to Pin 25 (together with resistor!)