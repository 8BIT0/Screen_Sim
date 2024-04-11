
import pygame

class Letter_Grid():
    def __init__(self, x, y, edge, def_color = [], slid_color = []):
        self.x = x
        self.y = y
        self.edge = edge
        self.select_state = False
        self.slid_color = slid_color
        self.def_color = def_color
        self.rect = pygame.Rect(self.x, self.y, self.edge, self.edge)

    def Rect(self):
        return self.rect
    
    def DefColor(self):
        return self.def_color

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
        self.grid_edge = 25
        self.width = self.grid_edge * self.grid_num
        self.height = self.grid_edge * self.grid_num
        self.grid_map = []
        cord_x = self.x
        cord_y = self.y
        self.map_rect = pygame.Rect(self.x - 1, self.y - 1, self.width + 2, self.height + 2)
        self.font = pygame.font.SysFont('Zpix', 300)
        # self.font = pygame.font.SysFont('DIN Condensed', 300)
        self.letter = self.font.render('', True, (255, 0, 0))
        print(self.map_rect)
        print(self.map_rect.center)
        for y in range(self.grid_num):
            cord_x = self.x
            for x in range(self.grid_num):
                self.grid_map.append(Letter_Grid(cord_x, cord_y, self.grid_edge, [0, 208, 208], [255, 255, 255]))
                cord_x += self.grid_edge
            cord_y += self.grid_edge

    def Letter_Display(self, letter = ''):
        self.letter = self.font.render(letter, True, (255, 0, 0))

    def clear(self):
        for y in range(self.grid_num):
            for x in range(self.grid_num):
                self.grid_map[x + (y * self.grid_num)].Set_Selected(False)

    def grid_metrix(self):
        return (self.grid_num, self.grid_num)

    def get_color_map(self):
        color_map = []
        for y in range(self.grid_num):
            for x in range(self.grid_num):
                # color = self.grid_map[x + (y * self.grid_num)].DefColor()
                # if self.grid_map[x + (y * self.grid_num)].Selected():
                color = int(self.grid_map[x + (y * self.grid_num)].Selected())
                color_map.append(color)
        return color_map

    def update(self, surf, event_list):
        mpos = pygame.mouse.get_pos()
        pygame.draw.rect(surf, [0, 208, 208], self.map_rect)
        pygame.draw.rect(surf, 'black', self.map_rect, 1)
        text_rect = self.letter.get_rect()
        text_rect.center = self.map_rect.center
        text_rect[0] = 85
        if text_rect[1] > -15:
            text_rect[1] = -15
        elif text_rect[1] >= -15:
            text_rect[1] = -40

        surf.blit(self.letter, text_rect)

        active = False
        for event in event_list:
            if event.type == pygame.MOUSEBUTTONDOWN:
                active = True
                break

        for y in range(self.grid_num):
            for x in range(self.grid_num):
                grid = self.grid_map[x + (y * self.grid_num)]

                slid = grid.Rect().collidepoint(mpos)
                if not grid.Selected():
                    if not slid:
                        line_width = 1
                        color = 'black'
                    else:
                        line_width = 0
                        color = grid.SlidColor()
                        if active:
                            grid.Set_Selected(True)
                else:
                    if active and slid:
                        line_width = 1
                        color = 'black'
                        grid.Set_Selected(False)

                if grid.Selected():
                    line_width = 0
                    color = grid.SlidColor()

                pygame.draw.rect(surf, color, grid.Rect(), line_width)
                pygame.draw.rect(surf, 'black', grid.Rect(), 1)

# pygame.init()
# clock = pygame.time.Clock()
# window = pygame.display.set_mode((640, 295))
# Grid = Letter_Grid_Map(10, 10, 11)

# run = True
# while run:
#     window.fill((255, 255, 255))

#     event_list = pygame.event.get()
#     for event in event_list:
#         if event.type == pygame.QUIT:
#             run = False
#     Grid.Letter_Display('S')
#     Grid.update(window, event_list)
#     pygame.display.flip()
#     clock.tick(60)
    
# pygame.quit()
# exit()