import pygame

class Text():
    def blitme(self, NEW_TEXT):
        self.update(NEW_TEXT)
        self.screen.blit(self.generated_text_image,self.generated_text_rect)
    def update(self, NEW_TEXT):
        NEW_TEXT = str(NEW_TEXT)
        self.generated_text_image = self.font.render(NEW_TEXT,True,self.color_text,self.color_background)
        self.generated_text_rect = self.generated_text_image.get_rect()
        if self.LEFT:
            self.generated_text_rect.left = self.LEFT
        if self.RIGHT:
            self.generated_text_rect.right = self.RIGHT
        if self.TOP:
            self.generated_text_rect.top = self.TOP
        if self.BOTTOM:
            self.generated_text_rect.bottom = self.BOTTOM
    def __init__(self,screen,NEW_TEXT,COLOR_TEXT,COLOR_BACKGROUND,FONT_SIZE,L,R,T,B):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.color_background = COLOR_BACKGROUND
        self.color_text = COLOR_TEXT
        self.font = pygame.font.SysFont(None, FONT_SIZE)
        self.LEFT = L
        self.RIGHT = R
        self.TOP = T
        self.BOTTOM = B
        self.update(NEW_TEXT)
