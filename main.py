import asyncio
import aioble
import lib.utils.decode as decode
import lib.utils.encode as encode
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
        bt.write_characteristic.write(encode.to_utf_8(value), send_update=True)
        print('WRITEN: ', value)
        await asyncio.sleep(1)            

# Tarefa para monitorar dados recebidos
async def _read_task():
    while True:
        try:
            connection, data = await bt.read_characteristic.written()
            print('READ: ', data)
            
            data_string = decode.to_string(data)
            print('as STRING: ', data_string)
            array_float = decode.to_array_float(data)
            print('as ARRAYFLOAT: ', array_float)
            array_short = decode.to_array_short(data)
            print('as ARRAYSHORT: ', array_short)
            array_byte = decode.to_array_byte(data)
            print('as ARRAYBYTE: ', array_byte)

        except Exception as e:
            print("Exception: ", e)

        finally:
            await asyncio.sleep_ms(100)

async def main():
    write_task = asyncio.create_task(_write_task())
    peripheral_task = asyncio.create_task(_peripheral_task())
    read_task = asyncio.create_task(_read_task())
    await asyncio.gather(write_task, peripheral_task, read_task)

aioble.register_services(bt.bt_service)
asyncio.run(main())