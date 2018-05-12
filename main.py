from utils.grid import Grid
from utils import extramath, pygame_utils
from PIDcontroller import PIDcontroller
import pygame, time


kV = 1
kT = 1
R = 1


def calc_motor_torque(velocity, voltage):
    return (voltage - (velocity / kV)) * kT / R

size = width, height = 1000, 1000
screen = pygame.display.set_mode(size)
screen.fill([255,255,255])

pid = PIDcontroller(100, .1, kI=.01, kD=.1)

for n in range(20000):
    pid.step(.01, screen)

pygame.display.flip()

while(True):
    time.sleep(1)



