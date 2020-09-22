from bluepy import btle
from datetime import datetime

device = btle.Peripheral()

class Delegate(btle.DefaultDelegate):
  def handleNotification(self, cHandle, data):    
    temperature_bytes = data[:2]
    humidity_bytes = data[2]
    temperature = int.from_bytes(temperature_bytes, byteorder="little") / 100.0
    humidity = humidity_bytes

    print("Tempterature: {}°C".format(temperature))
    print("    Humidity: {}%".format(humidity))
    print("        Time: {}".format(datetime.now().strftime("%H:%M:%S")))

try:  
  device.connect("A4:C1:38:4B:B7:FF")
  device.setDelegate(Delegate())
  ch = device.getCharacteristics(uuid="EBE0CCC1-7A0A-4B0C-8A1A-6FF2997DA3A6")[0]
  desc = ch.getDescriptors(forUUID=0x2902)[0]
  desc.write(0x01.to_bytes(2, byteorder="little"), withResponse=True)

  # waiting to notification
  while True:
    if not device.waitForNotifications(5.0):
      break

finally:
  device.disconnect()