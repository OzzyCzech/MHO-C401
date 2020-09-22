# Read Temperature and Huminidy from MHO-C401

MHO-C401 is new (2020) MMC E-Ink Screen Smart Bluetooth Thermometer Hygrometer BT2.0 Temperature Humidity Sensor from Xiaomi

* https://www.aliexpress.com/item/4001174769598.html
* https://www.gearbest.com/sale/MHO-C401/

## Battery level

```
Service <uuid=Battery Service handleStart=25 handleEnd=28>
 Characteristic <Battery Level>
 > UUID:  00002a19-0000-1000-8000-00805f9b34fb
 > HANDLE:  0x1b
 > SUPPORTS:  READ NOTIFY 
 > RESULTS  b'c'
```

## Temperature and humidity

```
 Characteristic <ebe0ccc1-7a0a-4b0c-8a1a-6ff2997da3a6>
 > UUID:  ebe0ccc1-7a0a-4b0c-8a1a-6ff2997da3a6
 > HANDLE:  0x36
 > SUPPORTS:  READ NOTIFY 
 > RESULTS  b'\x00\x00\x00'
```

3 bytes of data can

## Device units (READ, WRITE)

```txt
 Characteristic <ebe0ccbe-7a0a-4b0c-8a1a-6ff2997da3a6>
 > UUID:  ebe0ccbe-7a0a-4b0c-8a1a-6ff2997da3a6
 > HANDLE:  0x33
 > SUPPORTS:  READ WRITE 
 > RESULTS  b'\x00'
```

* `b'\x00'` - °C
* `b'\x01'` - °F