from lib.sensors.ahtx0 import AHT20
from lib.sensors.ens160 import ENS160
from machine import I2C, Pin
import utime

# I2C compartilhado (ajuste os pinos conforme seu hardware)
i2c = I2C(0, scl=Pin(5), sda=Pin(4))  # Exemplo

# Instância global dos sensores
aht = None
ens = None

def init_sensors():
    global aht, ens
    try:
        aht = AHT20(i2c)
        print(aht)
    except Exception as e:
        print("Erro ao iniciar AHT20:", e)
        aht = None

    try:
        ens = ENS160(i2c)
        print(ens)
    except Exception as e:
        print("Erro ao iniciar ENS160:", e)
        ens = None

def check_sensor_status():
    global aht, ens
    sensor_status = {
        "AHT20": False,
        "ENS160": False
    }

    if aht:
        try:
            _ = aht.temperature
            _ = aht.relative_humidity
            sensor_status["AHT20"] = True
        except:
            pass

    if ens:
        try:
            sensor_id = ens.get_id()
            if sensor_id != 0x0000:
                sensor_status["ENS160"] = True
        except:
            pass

    return sensor_status