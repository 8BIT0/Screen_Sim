from Screen_Obj import Virtial_Screen
import pygame

def main():
    v_Screen = Virtial_Screen.Virtial_Screen(240, 160, 2, [0, 208, 208])
    Quit = False

    # test code
    color_list = [[255, 255, 255], [169, 67, 145]]
    color_index = 0
    color = color_list[color_index]
    index = 0
    # test code

    while not Quit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Quit = True

        # test code
        for x in range(10, 20):
            for y in range(10, 20):
                v_Screen.set_pixel(x, y, color)

        if (index < 10):
            index += 1
        else:
            color_index += 1
            index = 0
            color = color_list[color_index % 2]
            # v_Screen.set_bg(color_list[(color_index + 1) % 2])
        # test code

        # draw all pixel brick
        v_Screen.display()

    v_Screen.quit()

main()