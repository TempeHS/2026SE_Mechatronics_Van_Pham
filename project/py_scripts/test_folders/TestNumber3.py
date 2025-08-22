import time
from PiicoDev_Ultrasonic import PiicoDev_Ultrasonic
from PiicoDev_Unified import sleep_ms
from ServoClassWUltra import RobotGO
from Ultrasonicdev import Ultrasonic

ultra = Ultrasonic()
robot = RobotGO()


def test():
        while True:
                robot.forward()
                print("Nice")
                if ultra.front.distance_mm < 200 and ultra.side.distance_mm > 300:
                        robot.stop()
                        robot.right()
                elif ultra.front.distance_mm < 200 and ultra.side.distance_mm < 300:
                        robot.stop()
                        robot.left()
robot.spin()
test()

