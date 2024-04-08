import pygame

class Pixel_Brick(object):
    def __init__(self, surface = ((0, 0), 0, 0, None), x = 0, y = 0, scale = 1, color = [255, 255, 255]):
        self.x = x
        self.y = y
        self.scale = scale
        self.color = color
        self.surface = surface
        pygame.draw.rect(self.surface, self.color, (self.x * self.scale, self.y * self.scale, self.scale, self.scale), 0)

    def set_color(self, color = [255, 255, 255]):
        self.color = color

    def update(self):
        pygame.draw.rect(self.surface, self.color, (self.x * self.scale, self.y * self.scale, self.scale, self.scale), 0)

    def get_color(self):
        return self.color
        
