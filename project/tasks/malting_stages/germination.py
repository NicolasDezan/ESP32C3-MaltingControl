from tasks.malting_task import malting_control
from lib.utils.uptime import Uptime; uptime = Uptime()
import asyncio
from data.actuators import valvula_entrada, valvula_saida, bomba_ar, rotacao

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
        rotacao.off()
        valvula_entrada.off()
        valvula_saida.on()
        bomba_ar.off()
        pass


async def time_control():
    import data.init_data as setpoint

    init_time = uptime.minutes()
    while (uptime.minutes() < (setpoint.germination_total_time*60 + init_time)):
        if malting_control["abort_flag"].is_set():
            print("! ABORTED GERMINATION !") 
        print(f"[DEBUG] Germination: {uptime.minutes() - init_time}/{setpoint.germination_total_time*60}")

        await asyncio.sleep(5)

    malting_control["current_stage"] = None


async def give_water():
    print("[DEBUG] OPEN DRAIN_VALVE") ;  valvula_saida.on()
    print("[DEBUG] AIR PUMP ON") ;  bomba_ar.on()

   
    while malting_control["current_stage"] == "germination":
        if malting_control["abort_flag"].is_set():
            print("! ABORTED GERMINATION GIVING WATER !")
            return
        
        init_time = uptime.seconds()
        print("[DEBUG] OPEN FILL_VALVE)") ; valvula_entrada.on()
        
        while (uptime.seconds() < (5 + init_time)):
            if malting_control["abort_flag"].is_set():
                print("! ABORTED DRAINING !")
                return
            print("[DEBUG] Giving water...")
            await asyncio.sleep(4)
        print("[DEBUG] CLOSE FILL_VALVE") ; valvula_entrada.off()

        init_time = uptime.seconds()
        print("[DEBUG] Waiting to give water...")
        while (uptime.seconds() < (5 + init_time)): # Esse trecho usa o tempo de adição de água
            if malting_control["abort_flag"].is_set():
                print("! ABORTED DRAINING !")
                return
            await asyncio.sleep(4)

    print("[DEBUG] CLOSE DRAIN_VALVE") ; valvula_saida.off()
    print("[DEBUG] AIR PUMP OFF") ;  bomba_ar.off()

async def temperature_control():
    while malting_control["current_stage"] == "germination":
        if malting_control["abort_flag"].is_set():
            print("! ABORTED GERMINATION TEMPERATURE CONTROL !")
            return
        print("[DEBUG] Temperature control loop is active")
        await asyncio.sleep(10.0)


async def rotation_control(): # Esse trecho usa o nivel de rotação
    while malting_control["current_stage"] == "germination":
        if malting_control["abort_flag"].is_set():
            print("! ABORTED ROTATION CONTROL !")
            return
        print("[DEBUG] Rotation is active") ; rotacao.on()
        await asyncio.sleep(12.5)