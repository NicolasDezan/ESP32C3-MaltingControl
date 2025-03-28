from tasks.malting_task import malting_control
from lib.utils.uptime import Uptime; uptime = Uptime()
import asyncio

async def germination_stage():
    """Etapa de germinação dos grãos"""
    malting_control["current_stage"] = "germination"
    print("=== GERMINATION STARTED ===")
    
    try:
        time_control_task = asyncio.create_task(time_control())
        temperature_control_task = asyncio.create_task(temperature_control())
        give_water_task = asyncio.create_task(give_water())
        rotation_control_task = asyncio.create_task(rotation_control())

        await asyncio.gather(
            time_control_task,
            temperature_control_task,
            give_water_task,
            rotation_control_task
        )

    except asyncio.CancelledError:
        print("! GERMINATION ABORTED !")

    finally:
        pass


async def time_control():
    import data.init_data as setpoint

    init_time = uptime.minutes()
    while (uptime.minutes() < (setpoint.germination_total_time*60 + init_time)):
        if malting_control["abort_flag"].is_set():
            print("! ABORTED GERMINATION !") 
        print(f"Germination: {uptime.minutes() - init_time}/{setpoint.germination_total_time*60}")

        await asyncio.sleep(5)


    malting_control["current_stage"] = None


async def give_water():
    print("OPEN DRAIN_VALVE")

    while malting_control["current_stage"] == "germination":
        if malting_control["abort_flag"].is_set():
            print("! ABORTED GERMINATION GIVING WATER !")
            return
        
        init_time = uptime.seconds()
        print("OPEN FILL_VALVE)")
        while (uptime.seconds() < (5 + init_time)): # Esse trecho usa o volume de água da germinação
            if malting_control["abort_flag"].is_set():
                print("! ABORTED DRAINING !")
                return
            print("Giving water...")
            await asyncio.sleep(4)
        print("CLOSE FILL_VALVE")

        init_time = uptime.seconds()
        print("Waiting to give water...")
        while (uptime.seconds() < (5 + init_time)): # Esse trecho usa o tempo de adição de água
            if malting_control["abort_flag"].is_set():
                print("! ABORTED DRAINING !")
                return
            await asyncio.sleep(4)

    print("CLOSE DRAIN_VALVE")


async def temperature_control():
    while malting_control["current_stage"] == "germination":
        if malting_control["abort_flag"].is_set():
            print("! ABORTED GERMINATION TEMPERATURE CONTROL !")
            return
        print("Controlling temperature...")
        await asyncio.sleep(2.5)


async def rotation_control(): # Esse trecho usa o nivel de rotação
    while malting_control["current_stage"] == "germination":
        if malting_control["abort_flag"].is_set():
            print("! ABORTED ROTATION CONTROL !")
            return
        print("Rotating...")
        await asyncio.sleep(5)