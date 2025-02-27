import asyncio
import utils.data_converter as dt
from tasks.parameters_tasks import change_parameters_task 

async def task_handler(data):
    try:
        array_byte = dt.decode_to_array_byte(data)

        
        if   array_byte[0] == 0:
            asyncio.create_task(change_parameters_task(array_byte))
        elif array_byte[0] == 1:
            asyncio.create_tast() # ...
        










    except Exception as e:
        print("ERROR in task_handler(): ", e)