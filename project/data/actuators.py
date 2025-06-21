from lib.actuators.actuator import Actuator
from data.consts_groups import WriteList
import lib.utils.bluetooth_config as bt

valvula_entrada = Actuator("Válvula de Entrada", 10)
valvula_saida = Actuator("Válvula de Saída", 6)
rotacao = Actuator("Rotação", 7)
resistencia = Actuator("Resistência", 8)
bomba_ar = Actuator("Bomba de Ar", 9)

actuators = {
    "entrada": valvula_entrada,
    "saida": valvula_saida,
    "rotacao": rotacao,
    "resistencia": resistencia,
    "bomba_ar": bomba_ar
}

def send_actuators_state():
    message = [
        WriteList.SEND_ACTUATORS,
        int(valvula_entrada.is_on()),
        int(valvula_saida.is_on()),
        int(rotacao.is_on()),
        int(resistencia.is_on()),
        int(bomba_ar.is_on())
    ]

    bt.write_characteristic.write(bytes(message), send_update=True)
    # print("Mensagem de atuadores enviada:", message)