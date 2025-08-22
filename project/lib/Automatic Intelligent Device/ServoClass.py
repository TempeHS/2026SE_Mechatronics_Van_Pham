import time
from servo import Servo
from machine import Pin, PWM
from PiicoDev_Ultrasonic import PiicoDev_Ultrasonic
from PiicoDev_Unified import sleep_ms

# create a PWM servo controller (16 - pin Pico)
class RobotGO():
    def __init__(self):
        self.servo_pwm = PWM(Pin(16))
        self.servo_pwm2 = PWM(Pin(18))
        self.side = PiicoDev_Ultrasonic(id=[0, 0, 0, 0])
        self.front = PiicoDev_Ultrasonic(id=[0, 0, 1, 0])
# Set the parameters of the servo pulses, more details in the "Documentation" section
        self.freq = 50
        self.min_us = 500
        self.max_us = 2500
        self.dead_zone_us = 1500
        self.ninedeg_turn = 2.6437
# create a servo object
        self.my_servo = Servo(pwm=self.servo_pwm, min_us=self.min_us, max_us=self.max_us, dead_zone_us=self.dead_zone_us, freq=self.freq)
        self.my_servo2 = Servo(pwm=self.servo_pwm2, min_us=self.min_us, max_us=self.max_us, dead_zone_us=self.dead_zone_us, freq=self.freq)

    def forward(self):
        self.my_servo.set_duty(1850)
        self.my_servo2.set_duty(1150)


    def right(self):
        self.my_servo.set_duty(1608)
        self.my_servo2.set_duty(1608)
        print("Right")
        time.sleep(self.ninedeg_turn)
        self.my_servo.stop()
        self.my_servo2.stop()
        time.sleep(2)

    def left(self):
        self.my_servo.set_duty(1387)
        self.my_servo2.set_duty(1387)
        print("Left")
        time.sleep(self.ninedeg_turn)
        self.my_servo.stop()
        self.my_servo2.stop()
        time.sleep(2)

    def spin(self):
        self.my_servo.set_duty(1600)
        self.my_servo2.set_duty(1800)

    def back(self):
        self.my_servo.set_duty(1150)
        self.my_servo2.set_duty(1850)
        time.sleep(2)
        self.my_servo.stop()
        self.my_servo2.stop()

    def stop(self):
        self.my_servo.stop()
        self.my_servo2.stop()


robot = RobotGO()
