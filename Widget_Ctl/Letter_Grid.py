import pygame

class Letter_Grid():
    def __init__(self, x, y, edge, slid_color = [], select_color = []):
        self.x = x
        self.y = y
        self.edge = edge
        self.select_state = False


class Letter_Grid_Map():
    def __init__(self, x = 0, y = 0, grid_num = 8):
        self.x = x
        self.y = y
        self.grid_num = grid_num
        self.grid_edge = 20
        self.width = self.grid_edge * self.grid_num
        self.height = self.grid_edge * self.grid_num
        self.rect = []
        for y in range(self.grid_num):
            for x in range(self.grid_num):
                self.rect.append(pygame.Rect(self.x + (x * self.grid_edge), self.y + (y * self.grid_edge), self.grid_edge, self.grid_edge))

    def update(self, surf, event_list):
        slid_color = []
        select_color = []
        mpos = pygame.mouse.get_pos()
        active = False
        for y in range(self.grid_num):
            for x in range(self.grid_num):
                rect = self.rect[x + (y * self.grid_num)]
                active = rect.collidepoint(mpos)
                pygame.draw.rect(surf, 'black', rect, 1 if not active else 0)


pygame.init()
clock = pygame.time.Clock()
window = pygame.display.set_mode((640, 480))
Grid = Letter_Grid_Map(10, 10, 8)

run = True
while run:
    window.fill((255, 255, 255))

    event_list = pygame.event.get()
    for event in event_list:
        if event.type == pygame.QUIT:
            run = False

    Grid.update(window, event_list)
    pygame.display.flip()
    clock.tick(60)
    
pygame.quit()
exit()
