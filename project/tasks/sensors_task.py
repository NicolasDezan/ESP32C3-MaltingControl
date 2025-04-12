import asyncio
from data.sensor_data import sensor_values
import lib.utils.bluetooth_config as bt
from lib.sensors.sensor_reader import get_sensor_readings
from data.consts_groups import WriteList


async def sensors_task():
    while True:
        temperature, humidity, co2 = get_sensor_readings()

        if temperature is not None and humidity is not None:
            sensor_values["temperature"] = temperature
            sensor_values["humidity"] = humidity

        if co2 is not None:
            sensor_values["eco2"] = co2

        temp = sensor_values.get("temperature")
        hum = sensor_values.get("humidity")
        eco2 = sensor_values.get("eco2")

        # Se algum valor estiver como None, usa zero como padrão
        temp = temp if temp is not None else 0.0
        hum = hum if hum is not None else 0.0
        eco2 = eco2 if eco2 is not None else 0

        # Quebra dos valores
        temp_int = int(temp)
        temp_dec = int((temp * 100) % 100)

        hum_int = int(hum)
        hum_dec = int((hum * 100) % 100)

        eco2_int = int(eco2)
        eco2_b1 = eco2_int // 10000
        eco2_b2 = (eco2_int % 10000) // 100
        eco2_b3 = eco2_int % 100

        message = [
            WriteList.SENSOR_VALUES,
            hum_int, hum_dec,
            temp_int, temp_dec,
            eco2_b1, eco2_b2, eco2_b3
        ]

        print("Sensors Message = ", message)

        bt.write_characteristic.write(bytes(message), send_update=True)

        await asyncio.sleep(5)