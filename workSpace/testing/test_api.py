import urequests

response = urequests.get(
  'http://api.weatherstack.com/current?access_key=53168372fda1b21d3bf1d596ba72973a&query=fetch:ip&hourly=1$interval=1'
)

print('yep')
