from bluepy import btle

device = btle.Peripheral()

try:  
  device.connect("A4:C1:38:4B:B7:FF")
  batteryLevel = device.getCharacteristics(uuid="00002a19-0000-1000-8000-00805f9b34fb")[0].read()
  print("Battery level: {}%".format(ord(batteryLevel)))

finally:
  device.disconnect()