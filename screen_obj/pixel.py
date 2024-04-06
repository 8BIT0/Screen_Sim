import tkinter as tk

class Pixel(object):
    def __init__(self, x = 0, y = 0, pixel_scale = 1, color = 0x0000, canvas = tk.Canvas):
        self.x = x
        self.y = y
        self.color = self.conv_color(color)
        self.canvas = canvas
        self.pixel_block = canvas.create_rectangle(x, y, x + pixel_scale, y + pixel_scale, outline = '')
        self.canvas.pack()

    def set_color(self, color = 0x0000):
        self.color = self.conv_color(color)
        self.canvas.itemconfigure(self.pixel_block, fill = self.color)

    def get_color(self):
        return self.color

    def conv_color(self, color = 0):
        return "#{}".format(self.hex_string(color, 6))

    def hex_string(self, num, length):
        return format(num, '0' + str(length) + 'x')