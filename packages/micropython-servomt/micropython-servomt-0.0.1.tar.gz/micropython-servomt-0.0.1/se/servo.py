import machine
import time


class Servo:
    def __init__(self, pin, pulsos_minimo=22, pulsos_maximo=122):
        self.pwm = machine.PWM(machine.Pin(pin), freq=50)
        angulo_neutro = 90
        self.antiangulo = 0
        self.pulsos_minimo = pulsos_minimo
        self.pulsos_maximo = pulsos_maximo
        self.angulo(angulo_neutro)
        time.sleep(1)

    def angulo(self, angulo):
        angulo_minimo = 0
        angulo_maximo = 180
        angulo = max(angulo_minimo, min(angulo, angulo_maximo))
        self.antiangulo = angulo
        self.pwm.duty(self.map(angulo, angulo_minimo, angulo_maximo, self.pulsos_minimo, self.pulsos_maximo))

    def map(self, x, in_min, in_max, out_min, out_max):
        return int((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)

    def exit(self):
        self.pwm.deinit()

    def reangulo(self):
        return self.antiangulo