from bluepy import btle
device = btle.Peripheral()
try:
  print("Connecting to device...")
  device.connect("A4:C1:38:4B:B7:FF") # need change your MAC address here 
  for service in device.getServices():
    print(str(service))
    for ch in service.getCharacteristics():
        if ch.supportsRead():
            print(" {}".format(ch))
            print(" > UUID: ", ch.uuid)
            print(" > HANDLE: ", hex(ch.getHandle()))
            print(" > SUPPORTS: ", ch.propertiesToString())
            if (ch.supportsRead()):
              try:
                print(" > RESULTS ", repr(ch.read()))
              except BTLEException as e:
                print(" > ERROR: ", e)
            print()
finally:
  device.disconnect