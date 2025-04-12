class ReadList:
    CHANGE_PARAMETERS = 0
    SEND_PARAMETERS = 1

class WriteList:
    SENSOR_VALUES = 2
    SEND_PARAMETERS = 1
    HEARTBEAT = 255


class ParametersCorrections:
    class Steeping:
        class SubmergedTime:
            MIN_VALUE = 1.0
            MULT_TEN = 1.0

        class WaterVolume:
            MIN_VALUE = 200.0
            MULT_TEN = 10.0

        class RestTime:
            MIN_VALUE = 0.0
            MULT_TEN = 0.1

        class Cycles:
            MIN_VALUE = 1.0
            MULT_TEN = 1.0

    class Germination:
        class RotationLevel:
            MIN_VALUE = 0.0
            MULT_TEN = 1.0

        class TotalTime:
            MIN_VALUE = 24.0
            MULT_TEN = 1.0

        class WaterVolume:
            MIN_VALUE = 100.0
            MULT_TEN = 1.0

        class WaterAddition:
            MIN_VALUE = 10.0
            MULT_TEN = 1.0

    class Kilning:
        class Temperature:
            MIN_VALUE = 40.0
            MULT_TEN = 1.0

        class Time:
            MIN_VALUE = 1.0
            MULT_TEN = 0.1