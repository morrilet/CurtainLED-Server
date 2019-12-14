import network

class WiFi(object):
  
  SSID = None
  PASS = None
  
  def __init__(self, SSID, PASS):
    self.SSID = SSID
    self.PASS = PASS
  
  def connect(self):
    station = network.WLAN(network.STA_IF)
    
    if station.isconnected():
      print('Already connected to WiFi')
      return
    
    station.active(True)
    station.connect(self.SSID, self.PASS)
    
    while station.isconnected() is False:
      # TODO: Timeout!
      pass
    
    print('Connected to WiFi.')
    print(station.ifconfig())
    
  def disconnect(self):
    station.disconnect()
    print('Disconnected from WiFi')
