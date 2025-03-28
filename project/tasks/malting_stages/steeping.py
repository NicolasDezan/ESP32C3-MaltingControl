from tasks.malting_task import malting_control
from lib.utils.uptime import Uptime; uptime = Uptime()
import asyncio

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
        print("...")


async def time_control():
    import data.init_data as setpoint

    cycle = 0
    
    while cycle < setpoint.steeping_cycles:
        cycle += 1
        print(f"\n[Cycle {cycle}/{setpoint.steeping_cycles}]")
        
        # 1. Encher água
        await fill_water()
        if malting_control["abort_flag"].is_set():
            print("! ABORTED DURING FILLING !")
            return
        
        # 2. Esperar tempo submerso
        print(f"Submerged for {setpoint.steeping_submerged_time}h")
        init_time = uptime.minutes()
        while (uptime.minutes() < (setpoint.steeping_submerged_time*60 + init_time)):
            if malting_control["abort_flag"].is_set():
                print("! ABORTED DURING SUBMERGED TIME !")
                return
            print(f"Submerged: {(uptime.minutes() - init_time)}/{setpoint.steeping_submerged_time*60}")

            await asyncio.sleep(1)

        # 3. Remover água - abrir valvula 
        await drain_water()
        if malting_control["abort_flag"].is_set():
            print("! ABORTED DURING DRAINING !")
            return
        
        # 4. Esperar tempo de descanso
        print(f"Resting for {setpoint.steeping_rest_time}h")
        init_time = uptime.minutes()
        while (uptime.minutes() < (setpoint.steeping_rest_time*60 + init_time)):
            
            if malting_control["abort_flag"].is_set():
                print("! ABORTED DURING REST TIME !")
                return
            print(f"Resting: {(uptime.minutes() - init_time)}/{setpoint.steeping_rest_time*60}")

            await asyncio.sleep(1)

    malting_control["current_stage"] = None

# IMPLEMENTAR A LOGICA DE CONVERTER VOLUME EM TEMPO DE VALVULA ABERTO
async def fill_water(): # Esse trecho usa o volume de água
    init_time = uptime.seconds()
    print("OPEN FILL_VALVE") # NESSA LINHA DEVE MANDAR ABRIR A VALVULA

    while (uptime.seconds() < (3 + init_time)):
        if malting_control["abort_flag"].is_set():
            print("! ABORTED DRAINING !")
            return        
        
        # SIMULAÇÃO DO TEMPO DE ENCHER
        print("Filling...")
        await asyncio.sleep(1)

    print("CLOSE FILL_VALVE") # NESSA LINHA DEVE MANDAR FECHAR A VALVULA

# IMPLEMENTAR A LOGICA DE CONVERTER VOLUME EM TEMPO DE VALVULA ABERTO
async def drain_water():
    init_time = uptime.seconds()
    print("OPEN DRAIN_VALVE") # NESSA LINHA DEVE MANDAR ABRIR A VALVULA DE DRENAGEM

    while (uptime.seconds() < (3 + init_time)):
        if malting_control["abort_flag"].is_set():
            print("! ABORTED DRAINING !")
            print("CLOSE DRAIN_VALVE") # !!! NECESSÁRIO CRIAR UM PROTOCOLO MELHORADO DE ABORTAR
            return
        
        # SIMULAÇÃO DO TEMPO DE ESVAZIAR
        print("Draining...")
        await asyncio.sleep(1)

    print("CLOSE DRAIN_VALVE")# NESSA LINHA DEVE MANDAR FECHAR A VALVULA DE DRENAGEM


async def temperature_control():
    while malting_control["current_stage"] == "steeping":
        if malting_control["abort_flag"].is_set():
            print("! ABORTED STEEPING TEMPERATURE CONTROL !")
            return
        print("Controlling temperature...")
        await asyncio.sleep(2.5)