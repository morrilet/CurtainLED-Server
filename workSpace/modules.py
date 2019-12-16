import time
import machine

class BaseModule(object):
  _name = None
  _enabled = False
  
  def __init__(self, name):
    self._name = name
  
  def handle_request(self, request):
    self._enabled = request.find('/?module={}'.format(self._name)) >= 0
  
  def loop(self):
    print('{} -- Active: {}'.format(self._name, self._enabled))
  
class TestModule(BaseModule):
  _led = machine.Pin(2, machine.Pin.OUT)
  _start_time = time.time()
  _elapsed_time = 0
  
  def __init__(self, name):
    super().__init__(name)
  
  def loop(self):
    if self._enabled:
      print(self._elapsed_time % 5)
      if self._elapsed_time % 5 == 0:
        if self._led.value() == 1:
          self._led.value(0)
        else:
          self._led.value(1)
      self._elapsed_time = time.time() - self._start_time
  



