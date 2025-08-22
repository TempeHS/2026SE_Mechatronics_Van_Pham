import time
from PiicoDev_Ultrasonic import PiicoDev_Ultrasonic
from PiicoDev_Unified import sleep_ms

class Ultrasonic:
    def __init__(self):
        self.side = PiicoDev_Ultrasonic(id=[0, 0, 0, 0])
        self.front = PiicoDev_Ultrasonic(id=[0, 0, 1, 0])
    
    def ultrarun(self):
        front = self.front.distance_mm
        side = self.side.distance_mm
        print(f"{front}, {side}")
        sleep_ms(250)



    def run(self):
            self.ultrarun()
            if self.front.distance_mm < 200 and self.side.distance_mm > 300:
                print("RIGHT")
                time.sleep(1)
            elif self.front.distance_mm < 200 and self.side.distance_mm < 300:
                print("LEFT")
                time.sleep(1)

if __name__ == "__main__":
    ultrarun = Ultrasonic()
    while True:
        ultrarun.ultrarun()
