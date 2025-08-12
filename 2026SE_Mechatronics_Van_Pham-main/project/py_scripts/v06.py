"""
Read distance from two PiicoDev Ultrasonic Rangefinders independently
"""


from PiicoDev_Ultrasonic import PiicoDev_Ultrasonic
from PiicoDev_Unified import sleep_ms

range_a = PiicoDev_Ultrasonic(id=[0, 0, 0, 0])
range_b = PiicoDev_Ultrasonic(id=[0, 0, 1, 0])

while True:

    print(f"{range_a.distance_mm}, {range_b.distance_mm}")

    sleep_ms(100)

