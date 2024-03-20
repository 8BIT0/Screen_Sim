import pixel as Pixel
from enum import Enum
import tkinter as tk
import time as Time

class Screen_Error(object):
    Error_None = 0
    UpdateAll_Size_Error = 1

class Screen(object):
    def __init__(self, screen_width = 0, screen_height = 0, scale = 1, bg_color = 0xFF0F):
        self.width = screen_width * scale
        self.height = screen_height * scale
        self.scale = scale
        self.bg_color = bg_color
        self.pixel_map = []
        self.window = tk.Tk()
        self.window.title("screen sim")
        self.window.resizable(width = False, height = False)
        self.window.geometry(str(self.width + 10) + 'x' + str(self.height + 12))
        self.canvas = tk.Canvas(self.window, width = self.width, height = self.height)
        self.canvas.pack()
        self.canvas.place(x=4, y = 4)
        for y in range(self.height):
            for x in range(self.width):
                single_pixel = Pixel.Pixel(x, y, scale, bg_color, self.canvas)
                single_pixel.set_color(0xBBCA)
                self.pixel_map.append(single_pixel)

    # all screen area fresh
    def update(self, color_map = []):
        if len(color_map) == len(self.pixel_map):
            index = 0
            for pixel_tmp in self.pixel_map:
                if pixel_tmp.get_color() != color_map[index]:
                    pixel_tmp.set_color(color_map[index])
                index += 1
            return Screen_Error.Error_None
        return Screen_Error.UpdateAll_Size_Error

    def get_pixel_size(self):
        return len(self.pixel_map)

    def display(self):
        self.window.update()

# Test Code
test = Screen(240,160, 1)
while True:
    test.display()
    Time.sleep(0.01)