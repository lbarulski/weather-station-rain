import time

import mip
import network
import machine
import esp32
import ujson
import requests

####################################
# --- CUSTOM (3d print) ---
# 11 cm -> r 55mm
# 9503 mm2 - pole powierzchni
# 1ml == 1000 mm3
# 1000/9503=x mm, 2500/9503=x mm
#
# --- MISOL: WH-SP-RG ---
# 0.3537 per tip
####################################

NETWORK_SSID="WB8"
NETWORK_PASS="1234567890"
NAME="J18"  # WB8

JSON_POST_URL="https://weather.barulski.dev/api/v1/rain-gauge/"+NAME

RAIN_GAUGE_CUSTOM_AREA_MM2 = 9503
RAIN_GAUGE_CUSTOM_ML_PER_TICK = 5

RAIN_GAUGE_WHSPRG_MM = 0.3537

# RAIN_GAUGE_TYPE = "custom"
RAIN_GAUGE_TYPE = "WH-SP-RG"

def main():
    print("Booting...")

    hall = machine.Pin(25, machine.Pin.IN)
    esp32.wake_on_ext0(pin=hall, level=esp32.WAKEUP_ANY_HIGH)

    if machine.wake_reason() == machine.PIN_WAKE:
        print("Woken up using hall sensor")
    else:
        print("Waiting few sec for potential debug...")
        time.sleep(5)
        print("Zzz...")
        machine.deepsleep()

    wifi()

    while True:
        print('Hall current value: ', hall.value())

        json_data = {
            "volume": round((RAIN_GAUGE_CUSTOM_ML_PER_TICK * 1000) / RAIN_GAUGE_CUSTOM_AREA_MM2, 1) if RAIN_GAUGE_TYPE == "CUSTOM" else RAIN_GAUGE_WHSPRG_MM,
        }

        print("POSTing data to {0}: {1}".format(JSON_POST_URL, ujson.dumps(json_data)))
        try:
            res = requests.post(JSON_POST_URL, data=ujson.dumps(json_data), headers={"Content-Type": "application/json"})
            print("POST response: %s" % res.text)
        except Exception as e:
            print(e)

        print("Zzz...")
        machine.deepsleep()


def wifi():
    print("Connecting to WIFI '%s'..." % NETWORK_SSID)
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(NETWORK_SSID, NETWORK_PASS)
    while not wlan.isconnected():
        pass
    print("Connected to WIFI '%s'" % NETWORK_SSID)
    print('IP addr: ', wlan.ifconfig()[0])

#### TRIGGERED MANUALLY VIA REPL ON FIRT INSTALL ####
def install_dependencies():
    mip.install("requests")

if __name__ == '__main__':
    main()
