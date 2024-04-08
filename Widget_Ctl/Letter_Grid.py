import pygame

class Letter_Grid():
    def __init__(self, x, y, edge, slid_color = []):
        self.x = x
        self.y = y
        self.edge = edge
        self.select_state = False
        self.slid_color = slid_color
        self.rect = pygame.Rect(self.x, self.y, self.edge, self.edge)

    def Rect(self):
        return self.rect
    
    def SlidColor(self):
        return self.slid_color
    
    def Selected(self):
        return self.select_state
    
    def Set_Selected(self, state = False):
        self.select_state = state

class Letter_Grid_Map():
    def __init__(self, x = 0, y = 0, grid_num = 8):
        self.x = x
        self.y = y
        self.grid_num = grid_num
        self.grid_edge = 20
        self.width = self.grid_edge * self.grid_num
        self.height = self.grid_edge * self.grid_num
        self.grid_map = []
        cord_x = self.x
        cord_y = self.y
        self.map_rect = pygame.Rect(self.x - 1, self.y - 1, self.width + 2, self.height + 2)
        for y in range(self.grid_num):
            cord_x = self.x
            for x in range(self.grid_num):
                self.grid_map.append(Letter_Grid(cord_x, cord_y, self.grid_edge, [138, 172, 150]))
                cord_x += self.grid_edge
            cord_y += self.grid_edge

    def update(self, surf, event_list):
        mpos = pygame.mouse.get_pos()
        pygame.draw.rect(surf, 'black', self.map_rect, 1)
        active = False
        if event_list.type == pygame.MOUSEBUTTONDOWN:
            active = True
        for y in range(self.grid_num):
            for x in range(self.grid_num):
                grid = self.grid_map[x + (y * self.grid_num)]
                slid = grid.Rect().collidepoint(mpos)
                if not slid:
                    line_width = 1
                    color = 'black'
                else:
                    line_width = 0
                    color = grid.SlidColor()

                pygame.draw.rect(surf, color, grid.Rect(), line_width)
                pygame.draw.rect(surf, 'black', grid.Rect(), 1)


pygame.init()
clock = pygame.time.Clock()
window = pygame.display.set_mode((640, 480))
Grid = Letter_Grid_Map(10, 10, 10)

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
