from bluepy import btle

device = btle.Peripheral()

try:
  device.connect("A4:C1:38:4B:B7:FF")

  # read by UUID
  deviceName = device.getCharacteristics(uuid="00002a00-0000-1000-8000-00805f9b34fb")[0].read()
  print("Device name: ", deviceName.decode('ascii'))

  # or by handle  
  print("Firmware: " , device.readCharacteristic(0x12).decode('ascii'))
  print("Hardware Revision: " , device.readCharacteristic(0x14).decode('ascii'))
  print("Manufacturer Name: " , device.readCharacteristic(0x18).decode('ascii'))

  # read battery level
  print("Battery level: {}%".format(ord(device.readCharacteristic(0x1b))))

  # read device units
  if (device.readCharacteristic(0x33) == b'\x00'):
    print('Units: °C')
  
  if (device.readCharacteristic(0x33) == b'\x01'):
    print('Units: °F')

finally:
  device.disconnect()