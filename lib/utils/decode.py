import struct

def to_string(data):
    try:
        if data:
            return data.decode('utf-8')  # Decodifica como string UTF-8
    except Exception as e:
        return None
    
def to_array_float(data):
    try:
        floats = struct.unpack('<' + 'f' * (len(data) // 4), data)
        return floats
    except Exception as e:
        print("Erro ao decodificar em ArrayFloat")
        return None
    
def to_array_short(data):
    try:
        # Modificar para 'h' no struct.unpack (cada short ocupa 2 bytes)
        shorts = struct.unpack('<' + 'h' * (len(data) // 2), data)
        return shorts
    except Exception as e:
        print("Erro ao decodificar em ArrayShort:", e)
        return None
    
def to_array_byte(data):
    try:
        # Converte o ByteArray para uma lista de inteiros
        byte_list = list(data)
        
        # Adiciona 128 a cada byte para retornar à faixa de 0 a 255
        unsigned_byte_list = [(b + 128) % 256 for b in byte_list]
        
        return unsigned_byte_list
    except Exception as e:
        print("Erro ao decodificar em ArrayByte:", e)
        return None