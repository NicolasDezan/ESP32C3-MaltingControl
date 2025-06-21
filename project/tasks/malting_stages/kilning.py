from tasks.malting_task import malting_control
from lib.utils.uptime import Uptime; uptime = Uptime()
import asyncio
from data.actuators import valvula_entrada, valvula_saida, rotacao, resistencia

async def kilning_stage():
    """Etapa de secagem dos grãos"""
    malting_control["current_stage"] = "kilning"
    print("=== KILNING STARTED ===")
    
    try:
        time_control_task = asyncio.create_task(kilning_time_control())
        temperature_control_task = asyncio.create_task(kilning_temperature_control())
        rotation_control_task = asyncio.create_task(kilning_rotation_control())

        await asyncio.gather(
            time_control_task,
            temperature_control_task,
            rotation_control_task
        )

    except asyncio.CancelledError:
        print("! KILNING ABORTED !")

    finally:
        rotacao.off()
        resistencia.off()
        pass


async def kilning_time_control():
    import data.init_data as setpoint

    init_time = uptime.minutes()
    while (uptime.minutes() < (setpoint.kilning_time*60 + init_time)):
        if malting_control["abort_flag"].is_set():
            print("! ABORTED KILNING !") 
            return
        
        print(f"[DEBUG] Kilning: {uptime.minutes() - init_time}/{setpoint.kilning_time*60}")
        await asyncio.sleep(5)


# Aqui deve ser usado o setpoint.kilning_temperature
async def kilning_temperature_control():
    """Controle simplificado da temperatura durante o kilning"""
    while malting_control["current_stage"] == "kilning":
        if malting_control["abort_flag"].is_set():
            print("! ABORTED KILNING TEMPERATURE CONTROL !")
            return
        
        resistencia.on()
        print("[DEBUG] High temperature control loop is active")
        
        await asyncio.sleep(2.5)

    malting_control["current_stage"] = None


# Rotação: básica
async def kilning_rotation_control():
    """Controle simplificado da rotação durante o kilning"""
    while malting_control["current_stage"] == "kilning":
        if malting_control["abort_flag"].is_set():
            print("! ABORTED KILNING ROTATION CONTROL !")
            return
        
        rotacao.on()

        print("[DEBUG] Rotation loop is active")
        
        await asyncio.sleep(5)