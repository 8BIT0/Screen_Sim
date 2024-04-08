import pygame

pygame.init()
clock = pygame.time.Clock()
window = pygame.display.set_mode((640, 480))

list1 = OptionBox(
    40, 40, 160, 40, (150, 150, 150), (100, 200, 255), pygame.font.SysFont(None, 30), 
    ["option 1", "2nd option", "another option"])

run = True
while run:
    clock.tick(60)
    event_list = pygame.event.get()
    for event in event_list:
        if event.type == pygame.QUIT:
            run = False

    selected_option = list1.update(event_list)
    if selected_option >= 0:
        print(selected_option)

    window.fill((255, 255, 255))
    list1.draw(window)
    pygame.display.flip()
    
pygame.quit()
exit()

