#!/usr/bin/python3from __future__ import print_function

import logging
logging.basicConfig()
logging.getLogger('pygatt').setLevel(logging.DEBUG)

import pygatt
import time
import sys

address = "D0:B5:C2:9F:8F:32"

adapter = pygatt.GATTToolBackend()
adapter.start()

while True:
   try:
      print("Connecting...")
      device = adapter.connect(address,3,pygatt.BLEAddressType.public)
      print("Connected")
      break
   except pygatt.exceptions.NotConnectedError:
      print("Not connected")
      time.sleep(1)
      continue

#device.subscribe('0000ffe1-0000-1000-8000-00805f9b34fb', callback = printNotification)

while True:
   try:
      time.sleep(1)
   except Exception as e:
      print(e)
