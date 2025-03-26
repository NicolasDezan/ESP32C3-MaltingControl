import asyncio
import utils.data_converter as dt
from tasks.parameters_tasks import change_parameters_task, send_parameters_task
from data.consts_groups import WriteList,ReadList

async def task_handler(data):
    try:
        array_byte = dt.decode_to_array_byte(data)

        
        if   array_byte[0] == ReadList.CHANGE_PARAMETERS:
            asyncio.create_task(change_parameters_task(array_byte))

        elif array_byte[0] == ReadList.SEND_PARAMETERS:
            asyncio.create_task(send_parameters_task(array_byte))
        

    except Exception as e:
        print("ERROR in task_handler(): ", e)