import time
from PiicoDev_Ultrasonic import PiicoDev_Ultrasonic
from PiicoDev_Unified import sleep_ms



print("van")

ultrarun = Ultrasonic()

while True:
    ultrarun.ultrarun()
    time.sleep(1)
