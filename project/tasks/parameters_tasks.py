import data.init_data as parameter

async def change_parameters_task(array_byte):
    print("_change_parameters_task() was CALLED: ", array_byte)

    parameter.steeping_submerged_time = array_byte[1]
    parameter.steeping_water_volume = array_byte[2]
    parameter.steeping_rest_time = array_byte[3]
    parameter.steeping_cycles = array_byte[4]

    parameter.germination_rotation_level = array_byte[5]
    parameter.germination_total_time = array_byte[6]
    parameter.germination_water_volume = array_byte[7]
    parameter.germination_water_addition = array_byte[8]

    parameter.kilning_temperature = array_byte[9]
    parameter.kilning_time = array_byte[10]

    parameter.rewrite_data()

    parameter.print_current_data()