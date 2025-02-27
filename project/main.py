import asyncio
import lib.aioble as aioble
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
        await asyncio.sleep(1)            

queue = asyncio.Queue() ; print("queue: ", queue)

# Tarefa para monitorar dados recebidos
async def _read_task():
    while True:
        try:
            connection, data = await bt.read_characteristic.written() ; print('READ: ', data)
            await queue.put(data) ; print("queue: ", queue)

        except Exception as e:
            print("Exception: ", e)

        #finally:
            #await asyncio.sleep_ms(100)

async def _process_task():
    while True:
        data = queue.get() ; print ("data: ", data)

        try:
            array_byte = dt.decode_to_array_byte(data)
            print('as ARRAYBYTE: ', array_byte)

            if array_byte[0] == 0:
                asyncio.create_task(_change_parameters_task(array_byte))
        except Exception as e:
            print("Exception_ArrayByte: ", e)

async def _change_parameters_task(array_byte):
    print("Mude os parametros!")

async def main():
    write_task = asyncio.create_task(_write_task())
    peripheral_task = asyncio.create_task(_peripheral_task())
    read_task = asyncio.create_task(_read_task())
    process_task = asyncio.create_task(_process_task())
    await asyncio.gather(write_task, peripheral_task, read_task, process_task)

aioble.register_services(bt.bt_service)
asyncio.run(main())