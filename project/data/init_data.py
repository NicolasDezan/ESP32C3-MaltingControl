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

# System Data
was_in_process = _loaded_data.get("was_in_process")

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