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
ninedeg_turn = 2.6437
# create a servo object
my_servo = Servo(pwm=servo_pwm, min_us=min_us, max_us=max_us, dead_zone_us=dead_zone_us, freq=freq
)

my_servo2 = Servo(pwm=servo_pwm2, min_us=min_us, max_us=max_us, dead_zone_us=dead_zone_us, freq=freq
)
servo_pwm = PWM(Pin(16))
servo_pwm2 = PWM(Pin(18))


def forward():
    my_servo.set_duty(2500)
    my_servo2.set_duty(500)
    time.sleep(10)

def right():
    my_servo.set_duty(1608)
    my_servo2.set_duty(1608)
    time.sleep(ninedeg_turn)


def left():
    my_servo.set_duty(1387)
    my_servo2.set_duty(1387)
    time.sleep(ninedeg_turn)


def back():
    my_servo.set_duty(500)
    my_servo2.set_duty(2500)
    time.sleep(10)


def stop():
    my_servo.stop()
    my_servo2.stop()
