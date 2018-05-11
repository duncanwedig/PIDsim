import math, pygame
import numpy as np
from utils.grid import Grid
from utils.extramath import lerp
from utils import pygame_utils


class FunctionDrawing(Grid):

    def __init__(self, window=((-10, 10), (-10, 10)), interval=1, step=.000001, color = (255,0,0)):

        self.color = color
        self.step = step

        super().__init__(window, interval)

        self.vectorized_func = np.vectorize(self.function)
        self.vectorized_draw = np.vectorize(self.draw_point)

        self.x_points = np.array([lerp(self.left, self.right, t) for t in np.arange(0, 1+step, step)])
        self.y_points = -self.vectorized_func(self.x_points)

        self.scaled_x = pygame_utils.scale_points(self.x_points, self.scale[0], self.screen_center[0])
        self.scaled_y = pygame_utils.scale_points(self.y_points, self.scale[1], self.screen_center[1])


    def function(self, x):
        return x

    def draw_point(self, x, y, screen):
        pygame.draw.circle(screen, self.color, (int(x),int(y)), 2)

    def draw_function(self, screen):
        self.draw_grid(screen)
        self.vectorized_draw(self.scaled_x, self.scaled_y, screen)