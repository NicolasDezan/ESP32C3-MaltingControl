import aioble
import bluetooth

NAME = "ESP32-BLE"

ADV_INTERVAL_MS = 250_000

BT_SERVICE_UUID = bluetooth.UUID('12345678-1234-1234-1234-1234567890ab')
bt_service = aioble.Service(BT_SERVICE_UUID)

BT_WRITE_UUID = bluetooth.UUID('12345678-1234-1234-1234-1234567890ac') 
write_characteristic = aioble.Characteristic(bt_service, BT_WRITE_UUID, read=True, notify=True)

BT_READ_UUID = bluetooth.UUID('12345678-1234-1234-1234-1234567890ad')
read_characteristic = aioble.Characteristic(bt_service, BT_READ_UUID, read=True, write=True, notify=True, capture=True)