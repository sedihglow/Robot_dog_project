from Control import *
from Action import *

class dog:
    def __init__(self):
        self.control = Control()
        self.action = Action()

    # move forward x steps
    def move_forward(self, steps):
        for i in range(steps):
            self.control.forWard()
        self.control.stop()

    #turn right x degrees 
    # TODO: Test this, might need a different range and not sure with stop()
    def turn_right(self, degree):
        for i in range(degree):
            self.control.attitude(0,0,i)
            time.sleep(0.1)
        self.control.stop()

    # turn left x degrees
    # TODO: Test this, might need a different range and not sure with stop()
    def turn_left(self, degree):
        for i in range(-degree):
            self.control.attitude(0,0,i)
            time.sleep(0.1)
        self.control.stop()
    
    def push_ups(self):
        self.action.push_ups()

