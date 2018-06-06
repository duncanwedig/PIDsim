from utils.grid import Grid
from utils import extramath, pygame_utils
from utils.motor import Motor
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

# pid = PIDcontroller(setpoint=100, kP=2.5, kI=0, kD=15, motor=Motor(312, .7, .71, 134))
# pid = PIDcontroller(setpoint=100, kP=5, kI=0.001, kD=15, motor=Motor(88.5, 2.7, 2.42, 133))
pid = PIDcontroller(setpoint=25, kP=4, kI=0.005, kD=1, motor=Motor(88.5, 2.7, 2.42, 133))

for n in range(4000):
    pid.step(.01, screen)

pygame.draw.line(screen, (0,0,255), (0,500), (1000, 500))

pygame.display.flip()

pid.motor.print_data()

while(True):
    time.sleep(1)



