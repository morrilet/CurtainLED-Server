import select
from Request import Request

class Connection(object):
  
  BUFFER_SIZE = 128
  ENCODING = 'utf-8'
  TIMEOUT = 5
  
  # Default HTML response format.
  _htmlFormat = '<html><head></head><body>{}</body></html>'
  
  def __init__(self, socket, address):
    self._socket = socket
    self._address = address
    
  def start(self):
    print('Starting listener for {}'.format(self._address))
    
    # Data from the socket. A list of strings to be joined later.
    data = []
    
    # Get the request data from the socket.
    self._socket.setblocking(0)
    self._socket.settimeout(self.TIMEOUT)
    while True:
      chunk = self._socket.recv(self.BUFFER_SIZE).decode(self.ENCODING)
      data.append(chunk)
      if len(chunk) < self.BUFFER_SIZE:
        break
    
    # Join the chunks into a cohesive request.
    request = "".join(data)
    print('REQUEST: {}'.format(request))
    
    # Process the request.
    r = Request(request)
    
    # Send the response.
    self._socket.send('HTTP/1.1 200 OK\n')
    self._socket.send('Content-Type: text/html\n')
    self._socket.send('Connection: close\n\n')
    self._socket.sendall(self._htmlFormat.format(r.POST))
    
    # Close the connection.
    self._socket.close()
    
    print('Closing listener for {}'.format(self._address))
