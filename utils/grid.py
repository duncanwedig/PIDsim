import pygame
import numpy as np
from utils.extramath import avg
from utils.pygame_utils import scale_points

drawline = pygame.draw.line

class Grid(object):

    def __init__(self, window=((-10, 10), (-10, 10)), interval=1):
        x,y = pygame.display.get_surface().get_size()
        self.screen_center = [x/2, y/2]
        self.scale = (x/(window[0][1]-window[0][0]), y/(window[0][1]-window[0][0]))
        self.lower = window[1][0]
        self.left = window[0][0]
        self.upper = window[1][1]
        self.right = window[0][1]
        self.scaled_lower = 0
        self.scaled_left = 0
        self.scaled_upper = y
        self.scaled_right = x
        self.x_axis = avg(self.lower, self.upper)
        self.y_axis = avg(self.left, self.right)
        self.scaled_xax = self.x_axis * self.scale[1] + self.screen_center[1]
        self.scaled_yax = self.y_axis * self.scale[0] + self.screen_center[0]

        self.interval = interval

        self.x_locations = np.array([x for x in np.arange(self.y_axis, self.right + self.interval, self.interval)])
        self.y_locations = np.array([y for y in np.arange(self.x_axis, self.upper + self.interval, self.interval)])

        self.original_lattice = np.array([[[x, y] for x in np.arange(self.left, self.right + self.interval, self.interval)]
                                for y in np.arange(self.lower, self.upper + self.interval, self.interval)])


    def draw_grid(self, screen, line_width=2, color=(0, 0, 0)):
        for x in scale_points(self.x_locations, self.scale[0], self.screen_center[0]):
            drawline(screen, color, (x, self.scaled_lower), (x, self.scaled_upper), line_width)
        for x in scale_points(-self.x_locations, self.scale[0], self.screen_center[0]):
            drawline(screen, color, (x, self.scaled_lower), (x, self.scaled_upper), line_width)
        for y in scale_points(self.y_locations, self.scale[1], self.screen_center[1]):
            drawline(screen, color, (self.scaled_left, y), (self.scaled_right, y), line_width)
        for y in scale_points(-self.y_locations, self.scale[1], self.screen_center[1]):
            drawline(screen, color, (self.scaled_left, y), (self.scaled_right, y), line_width)

        self.draw_axes(screen, color=color)

    def draw_axes(self, screen, line_width=4, color=(0, 0, 0)):
        drawline(screen, (0, 0, 255), (self.scaled_yax, self.scaled_lower), (self.scaled_yax, self.scaled_upper), line_width)
        drawline(screen, (0, 0, 255), (self.scaled_left * self.scale[0], self.scaled_xax), (self.scaled_right, self.scaled_xax), line_width)