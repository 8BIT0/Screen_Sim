import pygame

class Button():
    def __init__(self, x, y, width, height, state, hit_color = [], def_color = [], str = 'button'):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hit_state = state
        self.def_color = def_color
        self.hit_color = hit_color
        self.hit = True
        self.font = pygame.font.SysFont('Zpix', int(width / 8))
        self.text = self.font.render(str, True, (0, 0, 0))
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def get(self, surf, event_list):
        mpos = pygame.mouse.get_pos()
        slid = self.rect.collidepoint(mpos)
        state = False
        
        for event in event_list:
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.hit_state = True
            elif event.type == pygame.MOUSEBUTTONUP:
                if self.hit_state:
                    self.hit = True
                self.hit_state = False

        pygame.draw.rect(surf, self.def_color, self.rect, 0)
        if slid:
            if self.hit_state:
                pygame.draw.rect(surf, self.hit_color, self.rect, 0)
            if self.hit_state and self.hit:
                state = True
                self.hit = False
            
            pygame.draw.rect(surf, 'black', self.rect, 5)
        
        text_rect = self.text.get_rect()
        text_rect.center = self.rect.center
        surf.blit(self.text, text_rect)
        return state

# test code
# pygame.init()
# clock = pygame.time.Clock()
# window = pygame.display.set_mode((640, 295))
# button = Button(50, 50, 180, 50, False, [88, 127, 35], [100, 80, 100], 'Test_Button')

# run = True
# while run:
#     window.fill((255, 255, 255))

#     event_list = pygame.event.get()
#     for event in event_list:
#         if event.type == pygame.QUIT:
#             run = False
    
#     if button.get(window, event_list):
#         print('T')
    
#     pygame.display.flip()
#     clock.tick(60)
    
# pygame.quit()
# exit()





