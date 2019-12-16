class Request(object):
  
  GET = {}
  POST = {}
  
  def __init__(self, text):
    self.GET = self._parse_GET(text)
    self.POST = self._parse_POST(text)
  
  def _parse_GET(self, text):
    output = {}
    try:
      raw_get = text.split('/?')[1].split(' HTTP')[0].split('&')
      for param in raw_get:
        tokens = param.split('=')
        output[tokens[0]] = tokens[1]
    except IndexError as e:
      pass
    
    return output
  
  def _parse_POST(self, text):
    output = {}
    try:
      raw_post = text.split('\r\n\r\n')[1].split('&')
      for param in raw_post:
        tokens = param.split('=')
        output[tokens[0]] = tokens[1]
    except IndexError as e:
      pass
    
    return output
