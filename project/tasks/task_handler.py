import asyncio
import utils.data_converter as dt
from tasks.parameters_tasks import change_parameters_task, send_parameters_task
from data.consts_groups import WriteList,ReadList
from tasks.malting_task import malting_control

async def task_handler(data):
    try:
        array_byte = dt.decode_to_array_byte(data)

        
        if   array_byte[0] == ReadList.CHANGE_PARAMETERS:
            asyncio.create_task(change_parameters_task(array_byte))

        elif array_byte[0] == ReadList.SEND_PARAMETERS:
            asyncio.create_task(send_parameters_task(array_byte))
        
        elif array_byte[0] == ReadList.START_PROCESS:
            malting_control["active"] = True
            malting_control["abort_flag"].clear()

        elif array_byte[0] == ReadList.ABORT_PROCESS:
            malting_control["active"] = False
            malting_control["abort_flag"].set()

    except Exception as e:
        print("ERROR in task_handler(): ", e)