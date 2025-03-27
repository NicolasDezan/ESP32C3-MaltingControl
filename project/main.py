import asyncio
from tasks.bluetooth_tasks import peripheral_task, send_heartbeat_task, read_task
from tasks.malting_task import malting_task

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

    # Cria o loop principal juntando as tarefas
    await asyncio.gather(send_heartbeat, peripheral, read_data, malting)

# Inicia o loop principal
asyncio.run(main())