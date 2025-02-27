import asyncio
import aioble
import lib.utils.data_converter as dt
import lib.utils.bluetooth_config as bt

# Tarefa para lidar com conexões
async def _peripheral_task():
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


# Tarefa para escrever dados
async def _write_task():
    while True:
        value = 1
        bt.write_characteristic.write(dt.encode_to_utf_8(value), send_update=True)
        print('WRITEN: ', value)
        await asyncio.sleep(2)            


# Tarefa para monitorar dados recebidos
async def _read_task():
    while True:
        try:
            connection, data = await bt.read_characteristic.written()
            print('READ: ', data)
            array_byte = dt.decode_to_array_byte(data)

            if array_byte[0] == 0:
                asyncio.create_task(_change_parameters_task(array_byte))

        except Exception as e:
            print("Exception: ", e)


async def _change_parameters_task(array_byte):
    print("_change_parameters_task() was CALLED: ", array_byte)


async def main():
    write_task = asyncio.create_task(_write_task())
    peripheral_task = asyncio.create_task(_peripheral_task())
    read_task = asyncio.create_task(_read_task())
    await asyncio.gather(write_task, peripheral_task, read_task)


aioble.register_services(bt.bt_service)
asyncio.run(main())