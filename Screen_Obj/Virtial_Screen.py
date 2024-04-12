from Screen_Obj import Pixel_Brick
import pygame

class Virtial_Screen(object):
    def __init__(self, width = 240, height = 160, scale = 1, bg_color = [0, 208, 208]):
        self.width = width
        self.height = height
        self.pixel_scale = scale
        self.bg_color = bg_color
        self.pixel_map = []

        pygame.init()
        self.fresh = pygame.time.Clock()
        self.game_window = pygame.display.set_mode((self.width * self.pixel_scale, self.height * self.pixel_scale))
        
        for y in range(self.height):
            for x in range(self.width):
                pixel_tmp = Pixel_Brick.Pixel_Brick(self.game_window, x, y, scale, self.bg_color)
                self.pixel_map.append(pixel_tmp)

    def display(self):
        # display back ground color
        for x in range(self.width):
            for y in range(self.height):
                self.pixel_map[x + (y * self.width)].update()
        pygame.display.update()
        # pygame.dsiplay.flip()
        self.fresh.tick(60)

    def quit(self):
        pygame.quit()

    def set_color_map(self, color_map = [[0, 208, 208]]):
        if len(color_map) == (self.width * self.height):
            map_index = x + (y * self.width)
            for x in range(self.width):
                for y in range(self.height):
                    self.pixel_map[map_index].set_color(color_map[map_index])

    def set_pixel(self, x = 0, y = 0, color = [255, 255, 255]):
        if (x < self.width) and (x >= 0) and (y < self.height) and (y >= 0):
            self.pixel_map[x + (y * self.width)].set_color(color)

    def set_bg(self, color = [0, 208, 208]):
        self.bg_color = color
        for x in range(self.width):
            for y in range(self.height):
                self.pixel_map[x + (y * self.width)].set_color(self.bg_color)

    def get_bg(self):
        return self.bg_color
    
    def get_color_map(self):
        color_map = []
        for y in range(self.height):
            for x in range(self.width):
                color = self.pixel_map[x + (y * self.width)].get_color()
                color_map.append(color)
        return color_map
    
    def grid(self, state = False):
        self.grid = state

