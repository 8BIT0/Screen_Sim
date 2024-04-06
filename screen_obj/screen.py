import pixel as Pixel
from enum import Enum
import tkinter as tk
import time as Time

class Screen_Error(object):
    Error_None = 0
    UpdateAll_Size_Error = 1

class Screen(object):
    def __init__(self, screen_width = 0, screen_height = 0, scale = 1, bg_color = 0xBBCA):
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
        self.canvas.place(x = 4, y = 4)
        for y in range(self.height):
            for x in range(self.width):
                single_pixel = Pixel.Pixel(x, y, scale, bg_color, self.canvas)
                single_pixel.set_color(bg_color)
                self.pixel_map.append(single_pixel)
        self.window.after(1000, self.display)

        # test code
        self.index = 0
        self.dsp_color = [0x0000, 0xBBAA]
        self.dsp = 0
        self.default_color = self.dsp_color[self.dsp]
        # test code

        self.window.mainloop()

    # all screen area fresh
    def update(self, color_map = []):
        if len(color_map) == len(self.pixel_map):
            index = 0
            for pixel_tmp in self.pixel_map:
                if pixel_tmp.get_color() != color_map[index]:
                    pixel_tmp.set_color(color_map[index])
                index += 1
            self.display()
            return Screen_Error.Error_None
        return Screen_Error.UpdateAll_Size_Error

    def set_pixel(self, x = 0, y = 0, color = 0xBBAA):
        if (x >= 0) and (x < self.width) and (y >= 0) and (y < self.height):
            pixel = self.pixel_map[x + (y * self.width)]
            pixel.set_color(color)

    def get_pixel_size(self):
        return len(self.pixel_map)

    def display(self):
        for i in range(10, 20):
            for j in range(10, 20):
                self.set_pixel(i, j, self.default_color)

        self.index += 1
        if (self.index % 10) == 0:
            self.dsp = (self.dsp + 1) % 2
            self.default_color = self.dsp_color[(self.dsp + 1) % 2]

        self.window.after(10, self.display)
        # self.window.update()
        # self.window.mainloop()

# Test Code
test = Screen(240, 160, 1)
