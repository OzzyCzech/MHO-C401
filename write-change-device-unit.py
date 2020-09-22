from bluepy import btle

CODES_TO_UNITS = { b'\x00': 'C', b'\x01': 'F'}

device = btle.Peripheral()

try:
  device.connect("A4:C1:38:4B:B7:FF")
  ch = device.getCharacteristics(uuid="EBE0CCBE-7A0A-4B0C-8A1A-6FF2997DA3A6")[0]
  value = ch.read()

  print("Current units: °{}".format(CODES_TO_UNITS[value]))

  if (CODES_TO_UNITS[value] == 'C'):
    print("Switching to °F")
    ch.write(b'\x01', withResponse=True)
  else:
    print("Switching to °C")
    ch.write(b'\x00', withResponse=True)

finally:
  device.disconnect()