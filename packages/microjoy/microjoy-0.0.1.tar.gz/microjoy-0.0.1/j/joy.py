import machine
from time import sleep
from servo import Servo


class Joy:
    def __init__(self, pin, resolucao=4095, escala=(0, 180), invert=False):
        self.analog_pin = machine.ADC(machine.Pin(pin))
        self.analog_pin.atten(machine.ADC.ATTN_11DB)
        self.in_max = resolucao
        self.out_min = escala[0]
        self.out_max = escala[1]
        self.invert = invert

    def convert_linear_scale(self, value):
        x = ((value - 0) * (self.out_max - self.out_min)) / ((self.in_max - 0) + self.out_min)
        if self.invert:
            return self.out_max - x
        else:
            return x

    def read(self):
        return self.convert_linear_scale(self.analog_pin.read())