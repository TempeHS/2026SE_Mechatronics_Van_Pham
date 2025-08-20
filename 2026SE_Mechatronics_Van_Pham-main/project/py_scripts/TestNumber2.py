import time
from servo import Servo
from machine import Pin, PWM
from PiicoDev_Ultrasonic import PiicoDev_Ultrasonic
from PiicoDev_Unified import sleep_ms

# create a PWM servo controller (16 - pin Pico)
servo_pwm = PWM(Pin(16))
servo_pwm2 = PWM(Pin(18))
side = PiicoDev_Ultrasonic(id=[0, 0, 0, 0])
front = PiicoDev_Ultrasonic(id=[0, 0, 1, 0])
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



def forward():
    my_servo.set_duty(1700)
    my_servo2.set_duty(1300)
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
        print(f"{front.distance_mm}, {side.distance_mm}")
        time.sleep_ms(1)

def testing():
    while True:
        forward()
        ultrarun()
        if front.distance_mm < 200 and side.distance_mm > 200:
            print("RIGHT")
            stop()
            time.sleep(2)
            right()
        elif front.distance_mm < 200 and side.distance_mm < 200:
            print("LEFT")
            stop()
            time.sleep(2)
            left()



time.sleep(1)
testing()