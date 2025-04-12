import asyncio
from tasks.bluetooth_tasks import peripheral_task, send_heartbeat_task, read_task
from tasks.malting_task import malting_task
from tasks.sensors_task import sensors_task
from lib.sensors.sensor_checker import init_sensors, check_sensor_status
from lib.sensors.sensor_reader import get_sensor_readings
import data.init_data

def setup():
    print("Inicializando sensores...")
    init_sensors()
    status = check_sensor_status()
    print("Status dos sensores:", status)

    if not any(status.values()):
        print("Nenhum sensor disponível. Verifique a conexão.")
    else:
        if not status["AHT20"]:
            print("AHT20 não está funcionando corretamente.")
        if not status["ENS160"]:
            print("ENS160 não está funcionando corretamente.")

async def main():
    # Cria três tarefas assíncronas que serão executadas simultâneamente:
    
    # 1. Tarefa para enviar dados perdiodicamente a cada 2 segundos
    send_heartbeat = asyncio.create_task(send_heartbeat_task())
    
    # 2. Tarefa para gerenciamento do Bluetooth e suas conexões
    peripheral = asyncio.create_task(peripheral_task())
    
    # 3. Tarefa para recebimento e tratamento dos dados recebidos via Bluetooth
    read_data = asyncio.create_task(read_task())
    
    # 4. Tarefa para gerenciamento do processo de malteação
    malting = asyncio.create_task(malting_task())

    # 5. Tarefa para gerenciamento dos sensores
    sensors = asyncio.create_task(sensors_task())

    # Cria o loop principal juntando as tarefas
    await asyncio.gather(
        send_heartbeat, 
        peripheral, 
        read_data, 
        malting,
        sensors
    )

# Faz a inicialização e verificações necessárias
setup()

# Inicia o loop principal
asyncio.run(main())