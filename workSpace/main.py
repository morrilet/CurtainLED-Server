from WiFi import WiFi
from Server import Server

# Connect to WiFi.
wifi = WiFi('Morty', 'meatsleddd69_Morty')
wifi.connect()

# Spin up the server and start listening for requests.
server = Server()
server.start()
