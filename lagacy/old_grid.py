import pygame

pygame.init()
screen_width = 600
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Grid")
grid_gap = 5
numberOf_row = 15
numberOf_col = 15

grid_width = (screen_width - (grid_gap*(1 + numberOf_col)))//numberOf_col
grid_height = (screen_height - (grid_gap*(1 + numberOf_row)))//numberOf_row

initial_extra_gapx = screen_width - grid_width*numberOf_col - grid_gap*(1 + numberOf_col)
initial_extra_gapy = screen_height - grid_height*numberOf_row - grid_gap*(1 + numberOf_row)

startx = grid_gap + initial_extra_gapx//2

for i in range(numberOf_row):
    starty = grid_gap + initial_extra_gapy//2
    for j in range(numberOf_col):
        rect = pygame.draw.rect(screen, (255, 0, 0), (startx, starty, grid_width, grid_height))
        starty += grid_height + grid_gap
    startx += grid_width + grid_gap


def get_grid():
    
def highlight_rect():

    


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            highlight = True
        if event.type == pygame.MOUSEBUTTONUP:
            highlight = False

    
    pygame.display.update()
