import asyncio
from tasks.main_tasks import peripheral_task, send_heartbeat_task, read_task
import data.init_data as system_data

async def main():
    # Cria três tarefas assíncronas que serão executadas simultâneamente:
    
    # 1. Tarefa para enviar dados perdiodicamente a cada 2 segundos
    send_heartbeat = asyncio.create_task(send_heartbeat_task())
    
    # 2. Tarefa para gerenciamento do Bluetooth e suas conexões
    peripheral = asyncio.create_task(peripheral_task())
    
    # 3. Tarefa para recebimento e tratamento dos dados recebidos via Bluetooth
    read_data = asyncio.create_task(read_task())
    
    # Cria o loop principal juntando as tarefas
    await asyncio.gather(send_heartbeat, peripheral, read_data)

# Inicia o loop principal
asyncio.run(main())