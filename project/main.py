import asyncio
from tasks.main_tasks import peripheral_task, send_heartbeat_task, read_task
import data.init_data as system_data

async def main():
    send_heartbeat = asyncio.create_task(send_heartbeat_task())
    peripheral = asyncio.create_task(peripheral_task())
    read_data = asyncio.create_task(read_task())
    await asyncio.gather(send_heartbeat, peripheral, read_data)

asyncio.run(main())