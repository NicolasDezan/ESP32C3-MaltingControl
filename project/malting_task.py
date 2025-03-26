import asyncio

# Estado global simplificado
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
    """Orquestração das etapas de malteação"""
    await steeping_stage()

    if malting_control["abort_flag"].is_set():
        return
    
    await germination_stage()

    if malting_control["abort_flag"].is_set():
        return
    
    await kilning_stage()


async def steeping_stage():
    """Etapa de hidratação dos grãos"""
    malting_control["current_stage"] = "steeping"
    print("STEEPING Started")
    
    try:
        start = 0
        
        while start < 3:
            start = start + 1
            if malting_control["abort_flag"].is_set():
                return
            print("STEEPING Running")
            await asyncio.sleep(1)
        
        print("STEEPING Completed")
    
    finally:
        pass


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