from machine import Pin

class Actuator:
    def __init__(self, name: str, pin_number: int, active_high: bool = True):
        self.name = name
        self.pin = Pin(pin_number, Pin.OUT)
        self.active_high = active_high
        self.state = False
        self.off()

    def on(self):
        self.pin.value(1 if self.active_high else 0)
        self.state = True
        print(f"[ACTUATOR] {self.name} ligado")

    def off(self):
        self.pin.value(0 if self.active_high else 1)
        self.state = False
        print(f"[ACTUATOR] {self.name} desligado")

    def toggle(self):
        if self.state:
            self.off()
        else:
            self.on()

    def is_on(self):
        return self.state
