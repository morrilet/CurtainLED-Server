
try:
  import usocket as socket

except:
  import socket
import uasyncio as asyncio
from Modules import TestModule
from Connection import Connection

class Server(object):
  
  def __init__(self):
    # Open the socket.
    self._server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self._server.bind(('', 80))
    self._server.listen(5)
  
  def start(self):
    print('Starting server...')
    
    # Listen to the socket (asynchronously) forever.
    loop = asyncio.get_event_loop()
    loop.create_task(self.run())
    loop.run_forever()
  
  @asyncio.coroutine
  def run(self):
    
    while True:
      # Listen for connections.
      connection, address = self._server.accept()
      
      # Spin up a new listener thread with the connection info.
      listener = Connection(connection, address)
      listener.start()
      #connection.close()
      
      yield from asyncio.sleep(0.5)
    
    # Close the server.
    print('Stopping server.')
    self._server.close()
      
  def _get_query_params(self, request):
    pass



