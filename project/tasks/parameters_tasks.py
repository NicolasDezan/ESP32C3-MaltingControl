import data.init_data as parameter
from data.consts_groups import WriteList, ParametersCorrections
import asyncio

async def change_parameters_task(array_byte):
    print("change_parameters_task() was CALLED: ", array_byte)

    # Steeping
    parameter.steeping_submerged_time = (
        array_byte[1] * ParametersCorrections.Steeping.SubmergedTime.MULT_TEN
        + ParametersCorrections.Steeping.SubmergedTime.MIN_VALUE
    )
    parameter.steeping_water_volume = (
        array_byte[2] * ParametersCorrections.Steeping.WaterVolume.MULT_TEN
        + ParametersCorrections.Steeping.WaterVolume.MIN_VALUE
    )
    parameter.steeping_rest_time = (
        array_byte[3] * ParametersCorrections.Steeping.RestTime.MULT_TEN
        + ParametersCorrections.Steeping.RestTime.MIN_VALUE
    )
    parameter.steeping_cycles = (
        array_byte[4] * ParametersCorrections.Steeping.Cycles.MULT_TEN
        + ParametersCorrections.Steeping.Cycles.MIN_VALUE
    )

    # Germination
    parameter.germination_rotation_level = (
        array_byte[5] * ParametersCorrections.Germination.RotationLevel.MULT_TEN
        + ParametersCorrections.Germination.RotationLevel.MIN_VALUE
    )
    parameter.germination_total_time = (
        array_byte[6] * ParametersCorrections.Germination.TotalTime.MULT_TEN
        + ParametersCorrections.Germination.TotalTime.MIN_VALUE
    )
    parameter.germination_water_volume = (
        array_byte[7] * ParametersCorrections.Germination.WaterVolume.MULT_TEN
        + ParametersCorrections.Germination.WaterVolume.MIN_VALUE
    )
    parameter.germination_water_addition = (
        array_byte[8] * ParametersCorrections.Germination.WaterAddition.MULT_TEN
        + ParametersCorrections.Germination.WaterAddition.MIN_VALUE
    )

    # Kilning
    parameter.kilning_temperature = (
        array_byte[9] * ParametersCorrections.Kilning.Temperature.MULT_TEN
        + ParametersCorrections.Kilning.Temperature.MIN_VALUE
    )
    parameter.kilning_time = (
        array_byte[10] * ParametersCorrections.Kilning.Time.MULT_TEN
        + ParametersCorrections.Kilning.Time.MIN_VALUE
    )

    parameter.rewrite_data()

    from tasks.bluetooth_tasks import write_task
    
    asyncio.run(
        write_task([
            WriteList.SEND_PARAMETERS,

            # Steeping
            int((parameter.steeping_submerged_time - ParametersCorrections.Steeping.SubmergedTime.MIN_VALUE) / ParametersCorrections.Steeping.SubmergedTime.MULT_TEN),
            int((parameter.steeping_water_volume - ParametersCorrections.Steeping.WaterVolume.MIN_VALUE) / ParametersCorrections.Steeping.WaterVolume.MULT_TEN),
            int((parameter.steeping_rest_time - ParametersCorrections.Steeping.RestTime.MIN_VALUE) / ParametersCorrections.Steeping.RestTime.MULT_TEN),
            int((parameter.steeping_cycles - ParametersCorrections.Steeping.Cycles.MIN_VALUE) / ParametersCorrections.Steeping.Cycles.MULT_TEN),

            # Germination
            int((parameter.germination_rotation_level - ParametersCorrections.Germination.RotationLevel.MIN_VALUE) / ParametersCorrections.Germination.RotationLevel.MULT_TEN),
            int((parameter.germination_total_time - ParametersCorrections.Germination.TotalTime.MIN_VALUE) / ParametersCorrections.Germination.TotalTime.MULT_TEN),
            int((parameter.germination_water_volume - ParametersCorrections.Germination.WaterVolume.MIN_VALUE) / ParametersCorrections.Germination.WaterVolume.MULT_TEN),
            int((parameter.germination_water_addition - ParametersCorrections.Germination.WaterAddition.MIN_VALUE) / ParametersCorrections.Germination.WaterAddition.MULT_TEN),

            # Kilning
            int((parameter.kilning_temperature - ParametersCorrections.Kilning.Temperature.MIN_VALUE) / ParametersCorrections.Kilning.Temperature.MULT_TEN),
            int((parameter.kilning_time - ParametersCorrections.Kilning.Time.MIN_VALUE) / ParametersCorrections.Kilning.Time.MULT_TEN)
        ])
    )

    parameter.print_current_data()


async def send_parameters_task(array_byte):
    from tasks.bluetooth_tasks import write_task
    print("send_parameters_task() was CALLED: ", array_byte)

    asyncio.run(
        write_task([
            WriteList.SEND_PARAMETERS,

            # Steeping
            int((parameter.steeping_submerged_time - ParametersCorrections.Steeping.SubmergedTime.MIN_VALUE) / ParametersCorrections.Steeping.SubmergedTime.MULT_TEN),
            int((parameter.steeping_water_volume - ParametersCorrections.Steeping.WaterVolume.MIN_VALUE) / ParametersCorrections.Steeping.WaterVolume.MULT_TEN),
            int((parameter.steeping_rest_time - ParametersCorrections.Steeping.RestTime.MIN_VALUE) / ParametersCorrections.Steeping.RestTime.MULT_TEN),
            int((parameter.steeping_cycles - ParametersCorrections.Steeping.Cycles.MIN_VALUE) / ParametersCorrections.Steeping.Cycles.MULT_TEN),

            # Germination
            int((parameter.germination_rotation_level - ParametersCorrections.Germination.RotationLevel.MIN_VALUE) / ParametersCorrections.Germination.RotationLevel.MULT_TEN),
            int((parameter.germination_total_time - ParametersCorrections.Germination.TotalTime.MIN_VALUE) / ParametersCorrections.Germination.TotalTime.MULT_TEN),
            int((parameter.germination_water_volume - ParametersCorrections.Germination.WaterVolume.MIN_VALUE) / ParametersCorrections.Germination.WaterVolume.MULT_TEN),
            int((parameter.germination_water_addition - ParametersCorrections.Germination.WaterAddition.MIN_VALUE) / ParametersCorrections.Germination.WaterAddition.MULT_TEN),

            # Kilning
            int((parameter.kilning_temperature - ParametersCorrections.Kilning.Temperature.MIN_VALUE) / ParametersCorrections.Kilning.Temperature.MULT_TEN),
            int((parameter.kilning_time - ParametersCorrections.Kilning.Time.MIN_VALUE) / ParametersCorrections.Kilning.Time.MULT_TEN)
        ])
    )