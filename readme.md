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
ESP32: `Firebeetle ESP32-E V1.0`
Board: prototyped board

#### Rain Gauge (`Misol WH-SP-RG`)
Wires can be interchangeable (doesn't matter which is 1st and which 2nd)

`1st wire` from WH-SP-RG to `3.3V` on ESP32

`2nd wire` from WH-SP-RG to `Yellow pin` (separated with 10K Ohm from GND, connected with Green Wire on Board)

#### Board (Prototyped board)

`Black Wire` (`-`) to `GND` on ESP32

`Green Wire` to `Pin25` on ESP32

##### Old Description (DEPRECATED)
> Connect GND & PIN 25 via resistor 10K Ohm
> 
> Connect rain gauge 1st wire to 3.3V
> 
>Connect rain gauge 2nd wire to Pin 25 (together with resistor!)