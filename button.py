import pygame
green = (0, 255, 0)
class Text:
    def __init__(self,screen,color,text,posx,posy,fontsize=30):
        myfont = pygame.font.SysFont('Comic Sans MS',fontsize)
        self.textsurface = myfont.render(text,False,color)
        self.screen = screen
        self.posx, self.posy = posx,posy
        self.rect = pygame.Rect(self.posx, self.posy,self.textsurface.get_size()[0],self.textsurface.get_size()[1] )

    def update(self):

        self.screen.blit(self.textsurface, (self.posx, self.posy))

    def check_click(self,mouse_pos):
        mouse = pygame.Rect(mouse_pos[0],mouse_pos[1],10,10)
        return mouse.colliderect(self.rect)