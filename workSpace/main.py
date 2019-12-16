from WiFi import WiFi
from Server import Server
from Credentials import WiFi_Credentials

# Connect to WiFi.
wifi = WiFi(WiFi_Credentials['SSID'], WiFi_Credentials['PASS'])
wifi.connect()

# Spin up the server and start listening for requests.
#server = Server()
#server.start()
