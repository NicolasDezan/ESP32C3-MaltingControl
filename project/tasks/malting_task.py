import asyncio


# Estado global
malting_control = {
    "active": False,
    "current_stage": None,
    "abort_flag": asyncio.Event()
}


async def malting_task():
    # Loop principal que verifica se deve iniciar a malteação
    while True:
        # Aguarda o comando de início
        while not malting_control["active"]:
            await asyncio.sleep(1)
        try:
            # Loop principal do processo
            await execute_malting_stages()
            
        except asyncio.CancelledError:
            await finish_process()
        finally:
            await finish_process()


from tasks.malting_stages.steeping import steeping_stage
from tasks.malting_stages.germination import germination_stage
from tasks.malting_stages.kilning import kilning_stage
async def execute_malting_stages():
    print("=== MALTING STARTED ===")
    print("===       ...       ===")

    await steeping_stage()

    if malting_control["abort_flag"].is_set():
        return
    
    await germination_stage()

    if malting_control["abort_flag"].is_set():
        return
    
    await kilning_stage()


async def finish_process():
    """Reset básico do sistema"""
    print("FINISH PROCESS")
    malting_control["current_stage"] = None
    malting_control["abort_flag"].clear()
    malting_control["active"] = False


"""
Iniciar processo:
    malting_control["active"] = True
    malting_control["abort_flag"].clear()

Parar processo:
    malting_control["abort_flag"].set()"
"""