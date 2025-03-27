import asyncio
from lib.utils.uptime import Uptime; uptime = Uptime()

# Estado global
malting_control = {
    "active": False,
    "current_stage": None,
    "abort_flag": asyncio.Event()
}


async def malting_task():
    """Tarefa principal simplificada de malteação"""
    while True:
        # Aguarda o comando de início
        while not malting_control["active"]:
            await asyncio.sleep(0.1)

        try:
            # Loop principal do processo
            await execute_malting_stages()
            
        except asyncio.CancelledError:
            await finish_process()
        finally:
            await finish_process()


async def execute_malting_stages():
    await steeping_stage()

    if malting_control["abort_flag"].is_set():
        return
    
    await germination_stage()

    if malting_control["abort_flag"].is_set():
        return
    
    await kilning_stage()


async def steeping_stage():
    import data.init_data as setpoint
    malting_control["current_stage"] = "steeping"
    print("=== STEEPING STARTED ===")

    try:
        cycle = 0
        
        while cycle < setpoint.steeping_cycles:
            cycle += 1
            print(f"\n[Cycle {cycle}/{setpoint.steeping_cycles}]")
            
            # 1. Encher água - Correlação de tempo de valvula ligada e `setpoint.steeping_water_volume`
            print("Filling water...")
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
            print("Draining water...")
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
        
        print("\n=== STEEPING COMPLETED ===")
    
    finally:
        print("...")





async def germination_stage():
    """Etapa de germinação dos grãos"""
    malting_control["current_stage"] = "germination"
    print("GERMINATION Started")
    
    try:
        start = 0

        while start < 5:
            start = start + 1
            if malting_control["abort_flag"].is_set():
                return
            
            # CONTROLE AQUI!
            print("GERMINATION Running")
            await asyncio.sleep(1)
        
        print("GERMINATION Completed")
    
    finally:
        pass


async def kilning_stage():
    """Etapa de secagem/kilning"""
    malting_control["current_stage"] = "kilning"
    print("KILNING Started")
    
    try:
        start = 0

        while start < 2:
            start = start + 1
            if malting_control["abort_flag"].is_set():
                return
            
            # CONTROLE AQUI!
            print("KILNING Running")
            await asyncio.sleep(1)
        
        print("KILNING Completed")
    
    finally:
        pass


async def finish_process():
    """Reset básico do sistema"""
    print("FINISH PROCESS")
    malting_control["current_stage"] = None
    malting_control["abort_flag"].clear()
    malting_control["active"] = False


"""
            Como usar:

                Iniciar processo (em outra tarefa):
                    malting_control["active"] = True
                    malting_control["abort_flag"].clear()

                Parar processo (a qualquer momento):
                    malting_control["abort_flag"].set()"

"""