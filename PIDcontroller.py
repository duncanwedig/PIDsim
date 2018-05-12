from utils.grid import Grid
from utils import extramath, pygame_utils
import pygame, math, cmath
import numpy as np
from typing import Callable
from utils.vector import Vector, vectortype
from utils.motor import Motor

class PIDcontroller(object):

    def __init__(self, setpoint:float, kP:float, startpoint:float = 0, kI:float = 0, kD:float = 0,
                 opposingForce:Callable = lambda x:x, motor:Motor = Motor(1961, .7, .71, 134)):
        self.start_point = startpoint
        self.current_point = startpoint
        self.setpoint = setpoint
        self.error = self.setpoint - self.current_point

        self.velocity = 0
        self.acceleration = 0

        self.kP = kP
        self.kI = kI
        self.kD = kD

        self.Pterm = self.kP * self.error
        self.Iterm = 0
        self.Dterm = 0

        self.calcOpposingForce = opposingForce
        self.motor = motor

        self.current_time = 0

        self.previous_time = 0
        self.previous_error = self.error

        self.points = []

    def calcPID(self, timestep:float):

        # Error and times are updated here, rather than in the physics method.
        # This is partially to help simulate the behavior of a real PID controller.
        self.previous_error = self.error
        self.error = self.setpoint - self.current_point
        self.previous_time = self.current_time
        self.current_time += timestep

        self.Pterm = self.kP * self.error

        # I term is kI, multiplied by the area of the trapezoid formed by the current error, previous error,
        # and time differences.
        self.Iterm += self.kI * (self.error + self.previous_error) * (timestep) / 2
        self.Dterm = self.kD * (self.error - self.previous_error)/(timestep)

        return self.Pterm + self.Iterm + self.Dterm

    def calcPhysics(self, timestep:float, voltage:float):
        # This probably needs a better label, but simple implementations for now please
        self.acceleration = self.motor.get_torque(self.velocity, voltage)

        # If opposing force were actually used, arguments would be supplied here probably
        self.acceleration -= self.calcOpposingForce(0)

        # Kinematics to get from acceleration and start velocity to position
        self.current_point += (self.velocity * timestep) + (0.5 * self.acceleration * (timestep**2))
        self.velocity += self.acceleration * timestep

    def draw(self, screen):
        pointx = pygame_utils.scale_point(self.current_time, 5, 0)
        pointy = pygame_utils.scale_point(self.error, -5, 500)
        # point = pygame_utils.scale_points((self.current_time-100, -self.error), 5, 500)
        print(pointx, pointy)
        self.points.append(Vector((pointx,pointy), vectortype.XY))
        xy = self.points[-1].xy
        x = int(xy[0])
        y = int(xy[1])
        pygame.draw.circle(screen, (255,0,0), (x,y), 2)

    def step(self, timestep:float, screen:pygame.Surface):
        voltage = self.calcPID(timestep)
        self.calcPhysics(timestep, voltage)
        self.draw(screen)
        print("pos: ", self.current_point, "\nvelocity: ", self.velocity, "\nvoltage: ", voltage, "\naccel: ", self.acceleration)
        print("\n\nPterm: ", self.Pterm, "\nIterm: ", self.Iterm, "\nDterm: ", self.Dterm, "\n\n")
