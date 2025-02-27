import aioble
import bluetooth

BT_SERVICE_UUID = bluetooth.UUID('12345678-1234-1234-1234-1234567890ab')  # Serviço principal
BT_WRITE_UUID = bluetooth.UUID('12345678-1234-1234-1234-1234567890ac') 
BT_READ_UUID = bluetooth.UUID('12345678-1234-1234-1234-1234567890ad')

ADV_INTERVAL_MS = 250_000

NAME = "ESP32-BLE"

# Registro do servidor GATT
bt_service = aioble.Service(BT_SERVICE_UUID)

write_characteristic = aioble.Characteristic(
    bt_service, BT_WRITE_UUID, read=True, notify=True
)

read_characteristic = aioble.Characteristic(
    bt_service, BT_READ_UUID, read=True, write=True, notify=True, capture=True
)