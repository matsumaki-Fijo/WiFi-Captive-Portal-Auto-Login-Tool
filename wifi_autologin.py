import time
import subprocess
import requests
import os

# ------------ CONFIG ------------
WIFI_NAMES = ["IIITS_Student", "Hostel Student"]   # <-- both WiFi names here
FRIENDLY_NAMES = {
    "IIITS_Student": "College WiFi",
    "Hostel Student": "Hostel WiFi"
}

USERNAME = ""      # enter your username inside the brackets eg:- if your username is abc@iiits.in   then -->"abc@iits.in"
PASSWORD = ""      # your password
LOGIN_URL = "https://10.0.112.2:8090/login.xml"
# ---------------------------------

def get_connected_wifi():
    """Returns the name of the currently connected WiFi, or None."""
    try:
        output = subprocess.check_output(["netsh", "wlan", "show", "interfaces"]).decode()
        for line in output.split("\n"):
            if "SSID" in line and "BSSID" not in line:
                return line.split(":")[1].strip()
    except:
        return None

def login_portal():
    payload = {
        "mode": 191,
        "username": USERNAME,
        "password": PASSWORD,
        "a": int(time.time() * 1000),
        "producttype": 0
    }
    requests.packages.urllib3.disable_warnings()
    r = requests.post(LOGIN_URL, data=payload, verify=False)
    return r.text

# ------------ MAIN ------------
connected_wifi = get_connected_wifi()

if connected_wifi is None:
    os.system('cmd /c echo You are not connected to ANY WiFi! && pause')
    exit()

# Check if connected to either hostel or college network
if connected_wifi not in WIFI_NAMES:
    os.system(f'cmd /c echo Connected to "{connected_wifi}" but it is NOT a campus WiFi! && pause')
    exit()

# Login
response = login_portal()

# Success popup
os.system(f'cmd /c echo Logged in successfully on {FRIENDLY_NAMES[connected_wifi]}! && pause')

