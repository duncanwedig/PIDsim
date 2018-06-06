import math
from utils import extramath


class Motor(object):

    def __init__(self, free_speed:float, free_current:float, stall_torque:float,
                 stall_current:float, battery_voltage:float = 12):
        '''All input fields are SI units, probably.'''
        # self.free_speed = free_speed
        # self.free_current = free_current
        # self.stall_torque = stall_torque
        # self.stall_current = stall_current
        # self.battery_voltage = battery_voltage

        self.kT = stall_torque / stall_current
        self.R = battery_voltage / stall_current
        self.kV = (battery_voltage - free_current * self.R) / free_speed

    def get_torque(self, voltage:float, velocity:float):
        return ( voltage - (velocity * self.kV) ) * self.kT / self.R

    def print_data(self):
        print("kT: ", self.kT)
        print("kV: ", self.kV)
        print("R: ", self.R)
