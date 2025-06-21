from tasks.malting_task import malting_control
from lib.utils.uptime import Uptime; uptime = Uptime()
import asyncio
from data.actuators import valvula_entrada, valvula_saida, bomba_ar, rotacao

async def steeping_stage():
    malting_control["current_stage"] = "steeping"
    print("=== STEEPING STARTED ===")

    try:
        time_control_task = asyncio.create_task(time_control())
        temperature_control_task = asyncio.create_task(temperature_control())

        await asyncio.gather(
            time_control_task, 
            temperature_control_task
        )

        print("\n=== STEEPING COMPLETED ===")

    except asyncio.CancelledError:
        print("! STEEPING ABORTED !")

    finally:
        valvula_saida.on()
        valvula_entrada.off()
        print("...")


async def time_control():
    import data.init_data as setpoint

    cycle = 0
    
    while cycle < setpoint.steeping_cycles:
        cycle += 1
        print(f"\n[[DEBUG] Cycle {cycle}/{setpoint.steeping_cycles}]")
        
        # 1. Encher água
        await fill_water()
        if malting_control["abort_flag"].is_set():
            print("! ABORTED DURING FILLING !")
            return
        
        # 2. Esperar tempo submerso
        print(f"Submerged for {setpoint.steeping_submerged_time}h")
        init_time = uptime.seconds()
        while (uptime.seconds() < (setpoint.steeping_submerged_time*5 + init_time)):
            if malting_control["abort_flag"].is_set():
                print("! ABORTED DURING SUBMERGED TIME !")
                return
            print(f"[DEBUG] Submerged: {(uptime.seconds() - init_time)}/{setpoint.steeping_submerged_time*5}")

            await asyncio.sleep(1)

        # 3. Remover água - abrir valvula 
        await drain_water()
        if malting_control["abort_flag"].is_set():
            print("! ABORTED DURING DRAINING !")
            return
        
        # 4. Esperar tempo de descanso
        print(f"Resting for {setpoint.steeping_rest_time}h")
        init_time = uptime.seconds()
        while (uptime.seconds() < (setpoint.steeping_rest_time*5 + init_time)):
            
            if malting_control["abort_flag"].is_set():
                print("! ABORTED DURING REST TIME !")
                return
            print(f"[DEBUG] Resting: {(uptime.seconds() - init_time)}/{setpoint.steeping_rest_time*5}")

            await asyncio.sleep(1)

    malting_control["current_stage"] = None

async def fill_water():
    init_time = uptime.seconds()
    print("[DEBUG] OPEN FILL_VALVE") ;  valvula_entrada.on()

    while (uptime.seconds() < (3 + init_time)):
        if malting_control["abort_flag"].is_set():
            print("! ABORTED DRAINING !")
            return        
        
        # SIMULAÇÃO DO TEMPO DE ENCHER
        print("Filling...")
        await asyncio.sleep(1)

    print("[DEBUG] CLOSE FILL_VALVE") ;  valvula_entrada.off()

async def drain_water():
    init_time = uptime.seconds()
    print("[DEBUG] OPEN DRAIN_VALVE") ;  valvula_saida.on()

    while (uptime.seconds() < (3 + init_time)):
        if malting_control["abort_flag"].is_set():
            print("! ABORTED DRAINING !")
            print("[DEBUG] CLOSE DRAIN_VALVE") ;  valvula_saida.off()
            return
        
        print("[DEBUG] Draining...")
        await asyncio.sleep(1)

    print("[DEBUG] CLOSE DRAIN_VALVE") ;  valvula_saida.off()


async def temperature_control():
    while malting_control["current_stage"] == "steeping":
        if malting_control["abort_flag"].is_set():
            print("! ABORTED STEEPING TEMPERATURE CONTROL !")
            return
        print("[DEBUG] Temperature control loop is running")
        await asyncio.sleep(10.0)