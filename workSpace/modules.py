class BaseModule(object):
  _name = None
  _enabled = False
  
  def __init__(self, name):
    self._name = name
  
  def handleRequest(self, request):
    self._enabled = (
      request.find('/?module={}'.format(_name)) or 
      request.find('&module={}'.format(_name))
    )
  
  def loop(self):
    print('{} -- Active: {}'.format(self._name, self._enabled))
