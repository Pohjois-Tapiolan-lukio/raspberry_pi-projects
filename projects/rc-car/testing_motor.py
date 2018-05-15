import time
import threading

class TestingMotorDriver():
    DIST_PER_SEC  = 35.0 # cm/s default 35
    SEC_PER_TURN  = 2.087 # seconds per full turn (depending on the base material, use forwardLeft(), stop() and time.time() to measure the time)

    def __init__(self):
        pass

    def forward(self, left_speed, right_speed):
        print("Forward", left_speed, right_speed)

    def backward(self, left_speed, right_speed):
        print("Backward", left_speed, right_speed)

    def stop(self):
        print("Stop")

    def forwardDistance(self, dist):
        self.forward()
        threading.Timer(dist/self.DIST_PER_SEC, self.stop)

    def backwardDistance(self, dist):
        self.backward()
        threading.Timer(dist/self.DIST_PER_SEC, self.stop)
