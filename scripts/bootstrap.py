import mip
import network
import time

NETWORK_SSID="WB8"
NETWORK_PASS="1234567890"

print("--- Initiating connection to '%s' network" % NETWORK_SSID)

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(NETWORK_SSID, NETWORK_PASS)

while not wlan.isconnected():
    print("Waiting to establish network connection...")
    time.sleep(1)
    pass

print('IP addr: ', wlan.ifconfig()[0])
print("--- Network connection established successfully")

print("--- Installing dependencies")
mip.install("requests")
print("--- Dependencies installed successfully")