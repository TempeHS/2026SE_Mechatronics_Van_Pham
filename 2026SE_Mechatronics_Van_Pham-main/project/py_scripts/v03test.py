import time
from servo import Servo
from machine import Pin, PWM


# create a PWM servo controller (16 - pin Pico)
servo_pwm = PWM(Pin(16))
servo_pwm2 = PWM(Pin(18))

# Set the parameters of the servo pulses, more details in the "Documentation" section
freq = 50
min_us = 500
max_us = 2500
dead_zone_us = 1500

# create a servo object
my_servo = Servo(pwm=servo_pwm)
my_servo2 = Servo(pwm=servo_pwm2)

my_servo = Servo(
    pwm=servo_pwm, min_us=min_us, max_us=max_us, dead_zone_us=dead_zone_us, freq=freq
)

my_servo2 = Servo(
    pwm=servo_pwm2, min_us=min_us, max_us=max_us, dead_zone_us=dead_zone_us, freq=freq
)
class wheel:
    def __init__(self, pwm: PWM, min_us=500, max_us=2500, dead_zone_us=1500, freq=50,):
        self.pwm = pwm
        self._move_period_ms = 1000 // freq
        min_us = min_us if min_us > 0 else 0
        max_us = max_us if min_us < max_us < (1000 // freq) * 1000 else 0
        self._curr_duty = 0
        self.dead_zone_us = dead_zone_us

    def forward():
            my_servo.set_duty(2500)
            my_servo2.set_duty(500)
            time.sleep(2)
    
    def right():
            my_servo.set_duty(1600)
            my_servo2.set_duty(1600)
            time.sleep(2)

van = wheel()

van.right()