# WiFi Captive Portal Auto-Login Tool (Using Python)
This tool automates login to campus (IIIT sricity) WiFi networks that use a captive portal, removing the need to manually enter credentials in a browser.

## Features
- Logs into WiFi without opening a browser
- Supports multiple networks (College WiFi & Hostel WiFi)
- Simple one-click execution using a batch file
- Displays login confirmation in command prompt

## Requirements
- Python installed (3.x)
- `requests` library

Install dependency:
```bash
python -m pip install requests
```

## Setup Instructions

### 1. Download the script
Download `wifi_autologin.py` to your system.

### 2. Add your credentials
Open the script and edit:

```python
USERNAME = "your_username"
PASSWORD = "your_password"
```

### 3. Create a one-click launcher (.bat file)

Create a file named:

```
wifi_login.bat
```

Paste this inside it:

```
@echo off
"C:\Users\YourUsername\AppData\Local\Python\bin\python.exe" "%USERPROFILE%\Desktop\wifi_autologin.py"
```

Replace `YourUsername` with your actual Windows username if needed.
This is basically 
```
@echo off
"location of your python.exe file" "location of wifi_autologin.py file"
```

### 4. Run the tool

1. Connect to your campus WiFi  
2. Double-click `wifi_login.bat`  
3. You will be automatically logged in  


## How It Works
The script sends an HTTP POST request directly to the WiFi login portal with the user's credentials, bypassing the need for browser-based login. 
