try:
  import usocket as socket
except:
  import socket

class Server(object):

  # Default HTML response format.
  _htmlFormat = '<html><head></head><body>{}</body></html>'
  _server = None 
   
  # Create the server socket.
  def __init__(self):
    self._server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self._server.bind(('', 80))
    self._server.listen(5)

  def start(self):
    while True:
      conn, addr = self._server.accept()
      
      # Get the request.
      request = conn.recv(1024)
      request = str(request)
      
      # Log the connection.
      print('Got a connecton from {}'.format(str(addr)))
      print('Request: {}'.format(request))
      
      # Send the response.
      conn.send('HTTP/1.1 200 OK\n')
      conn.send('Content-Type: text/html\n')
      conn.send('Connection: close\n\n')
      conn.sendall(self._htmlFormat.format(str(request.find('/?module=test') or request.find('&module=test'))))
      
      # Close the connection.
      conn.close()
