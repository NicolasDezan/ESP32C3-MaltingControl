from lib.sensors.ahtx0 import AHT20
from lib.sensors.ens160 import ENS160
from machine import I2C, Pin
import utime

# Inicializa I2C (ajuste os pinos conforme necessário)
i2c = I2C(0, scl=Pin(5), sda=Pin(4))  # Exemplo

# Instancia sensores
aht = AHT20(i2c)
ens = ENS160(i2c)

def get_sensor_readings():
    try:
        # Leitura dos sensores
        temperature = aht.temperature  # °C
        humidity = aht.relative_humidity  # %
        co2 = ens.get_eco2()  # ppm

        return temperature, humidity, co2
    except Exception as e:
        print("Sensor read error:", e)
        return None, None, None
