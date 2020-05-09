import pygame
class Button():
    def __init__(self, size, color, position, text):
        self.size = size
        self.color = color
        self.position = position
        self.text = text

    def draw_button(self, screen):
        rect = pygame.Rect(self.position[0], self.position[1], self.size[0], self.size[1])
        pygame.draw.rect(screen, self.color, rect)
        # text
        font = pygame.font.Font('Arcade.ttf', int(self.size[0]*0.6))
        text = font.render(self.text, True, (255,255,255))
        screen.blit(text, (rect.left + int(rect.width*0.1), rect.top + int(rect.height*0.1)))


    def ishovering(self, pos):
        if pos[0] > self.position[0] and pos[0] < self.position[0] + self.size[0]:
            if pos[1] > self.position[1] and pos[1] < self.position[1] + self.size[1]:
                return True
        return False