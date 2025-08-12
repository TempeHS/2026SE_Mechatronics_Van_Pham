from machine import PWM

class ServoTrue():

    def __init__(
        self,
        pwm: PWM,
        min_us=500,
        max_us=2500,
        dead_zone_us=1500,
        freq=50,
        ninedeg_turn = 2.6437
    ):
            self.pwm = pwm
            self.pwm.freq(freq)
            self._move_period_ms = 1000 // freq
            min_us = min_us if min_us > 0 else 0
            max_us = max_us if min_us < max_us < (1000 // freq) * 1000 else 0
            self._curr_duty = 0
            self.dead_zone_us = dead_zone_us

    def forward(self):
        my_servo.set_duty(2500)
        my_servo2.set_duty(500)
        time.sleep(10)

    def right(self):
        my_servo.set_duty(1608)
        my_servo2.set_duty(1608)
        time.sleep(ninedeg_turn)


    def left(self):
        my_servo.set_duty(1387)
        my_servo2.set_duty(1387)
        time.sleep(ninedeg_turn)


    def back(self):
        my_servo.set_duty(500)
        my_servo2.set_duty(2500)
        time.sleep(10)


    def stop(self):
        my_servo.stop()
        my_servo2.stop()
