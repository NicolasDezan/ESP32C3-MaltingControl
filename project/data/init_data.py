import ujson
from data.default_data import default_data as _default

def _read_data(_dir,_file_name):
    try:
        with open(_dir + _file_name, "r") as f:
            return ujson.load(f)
    except Exception as e:
        print("ERROR in read_data(): ", e)
        return {}

def _write_data(_dir,_file_name,_data):
    try:
        with open(_dir+_file_name, "w") as f:
            ujson.dump(_data, f)
    except Exception as e:
        print("FATAL in write_data(default): ", e)
        return {}

_dir = "data/"
_file_name = "config.json"

_loaded_data = _read_data(_dir,_file_name)

if(_loaded_data == {}):
    _write_data(_dir,_file_name,_default)
    _loaded_data = _read_data(_dir,_file_name)

# System Data -> Comentado: aplicação futura para lidar com interrupções do processo
# was_in_process = _loaded_data.get("was_in_process")

# Steeping
steeping_submerged_time = _loaded_data.get("steeping_submerged_time")
steeping_water_volume = _loaded_data.get("steeping_water_volume")
steeping_rest_time = _loaded_data.get("steeping_rest_time")
steeping_cycles = _loaded_data.get("steeping_cycles")

# Germination
germination_rotation_level = _loaded_data.get("germination_rotation_level")
germination_total_time = _loaded_data.get("germination_total_time")
germination_water_volume = _loaded_data.get("germination_water_volume")
germination_water_addition = _loaded_data.get("germination_water_addition")

# Kilning
kilning_temperature = _loaded_data.get("kilning_temperature")
kilning_time = _loaded_data.get("kilning_time")

def rewrite_data():
    _current_data = {
    # "was_in_process": was_in_process,
    
    "steeping_submerged_time": steeping_submerged_time,
    "steeping_water_volume": steeping_water_volume,
    "steeping_rest_time": steeping_rest_time,
    "steeping_cycles": steeping_cycles,

    "germination_rotation_level": germination_rotation_level,
    "germination_total_time": germination_total_time,
    "germination_water_volume": germination_water_volume,
    "germination_water_addition": germination_water_addition,

    "kilning_temperature": kilning_temperature,
    "kilning_time": kilning_time
    }
    _write_data(_dir,_file_name,_current_data)

def print_current_data():
    print("----------------------------------------")
    print("             Current Data               ")
    print("----------------------------------------")
    # print()    
    # print(f"SystemData  - was_in_process: {was_in_process}")
    print()
    print(f"Steeping    - submerged_time: {steeping_submerged_time}")
    print(f"Steeping    - water_volume: {steeping_water_volume}")
    print(f"Steeping    - rest_time: {steeping_rest_time}")
    print(f"Steeping    - cycles: {steeping_cycles}")
    print()
    print(f"Germination - rotation_level: {germination_rotation_level}")
    print(f"Germination - total_time: {germination_total_time}")
    print(f"Germination - water_volume: {germination_water_volume}")
    print(f"Germination - water_addition: {germination_water_addition}")
    print()
    print(f"Kilning     - temperature: {kilning_temperature}")
    print(f"Kilning     - time: {kilning_time}")
    print()
    print("----------------------------------------")

print_current_data()