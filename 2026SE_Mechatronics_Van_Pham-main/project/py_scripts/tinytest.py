import time
from servo import Servo
from machine import Pin, PWM
from PiicoDev_Ultrasonic import PiicoDev_Ultrasonic
from PiicoDev_Unified import sleep_ms

# create a PWM servo controller (16 - pin Pico)
servo_pwm = PWM(Pin(16))
servo_pwm2 = PWM(Pin(18))
range_a = PiicoDev_Ultrasonic(id=[0, 0, 0, 0])
range_b = PiicoDev_Ultrasonic(id=[0, 0, 1, 0])
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
    time.sleep(2)

def right():
    my_servo.set_duty(1608)
    my_servo2.set_duty(1608)
    time.sleep(ninedeg_turn)
    my_servo.stop()
    my_servo2.stop()
    time.sleep(2)

def left():
    my_servo.set_duty(1387)
    my_servo2.set_duty(1387)
    time.sleep(ninedeg_turn)
    my_servo.stop()
    my_servo2.stop()
    time.sleep(2)

def back():
    my_servo.set_duty(500)
    my_servo2.set_duty(2500)
    time.sleep(2)
    my_servo.stop()
    my_servo2.stop()

def stop():
    my_servo.stop()
    my_servo2.stop()

def ultrarun():
    while True:
        print(f"{range_a.distance_mm}, {range_b.distance_mm}")
        sleep_ms(100)

def testing():
    forward()
    ultrarun()
    if range_b <= "500":
        left()
    stop()

left()
testing()