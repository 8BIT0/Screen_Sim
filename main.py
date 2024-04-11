from Screen_Obj import Virtial_Screen
import Font.Font_11x11 as F_11 
import pygame

def main():
    v_Screen = Virtial_Screen.Virtial_Screen(240, 160, 1, [0, 208, 208])
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
        x = 10
        y = 10
        for l in F_11.get_Letter_List():
            for x_t in range(x, x + 11):
                for y_t in range(y, y + 11):
                    if l[1][y_t - y][x_t - x] == 1:
                        v_Screen.set_pixel(x_t, y_t, 'white')
            x += 6
            if x > 160:
                y += 11
                x = 10
        
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