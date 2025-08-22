"""
Read distance from two PiicoDev Ultrasonic Rangefinders independently
"""


from PiicoDev_Ultrasonic import PiicoDev_Ultrasonic
from PiicoDev_Unified import sleep_ms

side = PiicoDev_Ultrasonic(id=[0, 0, 0, 0])
front = PiicoDev_Ultrasonic(id=[0, 0, 1, 0])

while True:

    print(f"{front.distance_mm}, {side.distance_mm}")

    sleep_ms(100)

