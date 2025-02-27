import aioble
import asyncio
import lib.utils.bluetooth_config as bt
from lib.utils.task_handler import task_handler

# Tarefa para lidar com conexões
async def peripheral_task():
    while True:
        try:
            async with await aioble.advertise(
                bt.ADV_INTERVAL_MS, name=bt.NAME, services=[bt.BT_SERVICE_UUID]
            ) as connection:
                connected_device = connection.device
                print("CONNECTED: ", connected_device)
                # Aguarda a desconexão
                await connection.disconnected()
                print("DISCONNECTED: ", connected_device)
        except Exception as e:
            print("Erro na tarefa periférica: ", e)
        finally:
            await asyncio.sleep_ms(100)


# Tarefa para monitorar dados recebidos
async def read_task():
    while True:
        try:
            connection, data = await bt.read_characteristic.written()
            asyncio.create_task(task_handler(data))

        except Exception as e:
            print("ERROR in read_task(): ", e)


# Envia uma constante a cada 2 segundos
async def send_heartbeat_task():
    while True:
        bt.write_characteristic.write(bytes(255), send_update=True)
        await asyncio.sleep(2)