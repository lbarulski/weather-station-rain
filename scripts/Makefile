# Default target
.DEFAULT_GOAL := done

flash:
	echo "--- Flashing ESP32"
	esptool.py --chip esp32 --port /dev/tty.wchusbserial2140 erase_flash
	sleep 2
	echo "--- Loading ESP32 Micropython firmware"
	esptool.py --chip esp32 --port /dev/tty.wchusbserial2140 --baud 460800 write_flash -z 0x1000 ESP32_GENERIC-20240222-v1.22.2.bin
	sleep 2
	echo "--- Firmware loaded successfully"

bootstrap: flash
	echo "--- Bootstrapping environment"
	ampy -p /dev/tty.wchusbserial2140 -b 115200 run bootstrap.py
	echo "--- Environment bootstrapped successfully"

upload: bootstrap
	echo "--- Uploading script"
	ampy -p /dev/tty.wchusbserial2140 -b 115200 put ../main.py
	echo "--- Script uploaded successfully"

done: upload
	echo "\033[0;32m--- ESP32 ready ---\033[0m"

.PHONY: upload bootstrap flash done