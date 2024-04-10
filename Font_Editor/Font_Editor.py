import pygame
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import Widget_Ctl.Letter_Grid as Letter_Grid_Map
import Widget_Ctl.Button as Button

Letter = 'abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ`~!@#$%^&*()_+-=[]{}\\|;:\'",.<>/?'

pygame.init()
clock = pygame.time.Clock()
window = pygame.display.set_mode((295, 440))
Grid = Letter_Grid_Map.Letter_Grid_Map(10, 10, 11)
Comfirm_Button = Button.Button(9, 288, 277, 48, False, [88, 127, 35], [100, 80, 100], 'Convert')
Nxt_Button = Button.Button(9, 338, 277, 48, False, [88, 127, 35], [100, 80, 100], 'Nxt')
Pre_Button = Button.Button(9, 388, 277, 48, False, [88, 127, 35], [100, 80, 100], 'Pre')

run = True
letter_cnt = 0
while run:
    window.fill((255, 255, 255))

    event_list = pygame.event.get()
    for event in event_list:
        if event.type == pygame.QUIT:
            run = False

    Comfirm_Button.get(window, event_list)
    if Nxt_Button.get(window, event_list):
        Grid.clear()
        letter_cnt += 1
        if letter_cnt >= len(Letter):
            letter_cnt = 0
        print('letter_cnt', letter_cnt)

    if Pre_Button.get(window, event_list):
        Grid.clear()
        letter_cnt -= 1
        if letter_cnt + len(Letter) == 0:
            letter_cnt = 0
        print('letter_cnt', letter_cnt)

    Grid.Letter_Display(Letter[letter_cnt])
    Grid.update(window, event_list)
    pygame.display.flip()
    clock.tick(60)
    
pygame.quit()
exit()


