# CurtainLED-Server
A simple MicroPython back-end for controlling Neopixels.

## Key Principles

#### WiFi.py
A simple interface for connecting to wifi networks. This is used in main.py to initialize a connection.

#### Server.py
A bare-bones server implementation using [Python sockets](https://docs.python.org/3/library/socket.html). This is how devices on the network will send requests to the LEDs. Will act as a simple REST API.

#### Modules
Responsible for driving the LEDs. Each module will be enabled / disabled by name via the REST API. Conceptually, modules are self-contained LED effects that can be plugged into the server and run in the listen loop. They will all inherit from BaseModule.

#### TODO
- Un-tracked configuration files for SSIDs, passwords, etc.
- Querystring parsing in the server.
