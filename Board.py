import pygame

pygame.init()



class Grid():
    color = (0, 0, 0)
    def __init__(self, screen_height, screen_width, rows, columns):
        self.rows = rows
        self.columns = columns

        self.grid_width = screen_width//columns #dividing equal pixels 
        assert (screen_width % columns !=1), "modify screen width or noumber of columns"

        self.grid_height = screen_height//rows
        assert (screen_height % rows !=1), "modify screen height or noumber of rows"

    def clicked(self, pos):
        row_index = pos[1]//self.grid_height
        column_index = pos[0]//self.grid_width
        return (row_index, column_index)        

    def drawGrid(self, screen):
        for i in range(self.rows):
            pygame.draw.line(screen, Grid.color, (0, i*self.grid_height), (self.rows*self.grid_width, i*self.grid_height))
        for i in range(self.columns + 1):
            pygame.draw.line(screen, Grid.color, (i*self.grid_width, 0), (i*self.grid_width, self.columns*self.grid_width))



class Tiles():

    def __init__(self, grid_width, grid_height, index, color1, color2, color3, color4, parent=None):
        self.width = grid_width
        self.height = grid_height
        self.index = index
        self.empty_color, self.wall_color, self.explored_color = color1, color2, color3
        self.recently_discovered_color = color4
        self.color = self.empty_color
        self.type = 1 # wall--0; empty--1; explored--2; newly discovered-- -1
        self.parent = parent
        self.text = None

    def makeWall(self):
        self.color = self.wall_color
        self.type = 0

    def makeNewlyDiscovered(self, parent):
        self.color = self.recently_discovered_color
        self.type = -1
        self.parent = parent

    def makeExplored(self):
        if type(self.type) == int:
            self.color = self.explored_color 
            self.type = 0

    def makepath(self):
        self.color = (150,100,150)
        
    def makeStartEnd(self, type): # MAKE START/END ICONS
        self.color = (0, 0, 0)
        self.type = type # 'end' and 'start'

    def drawTile(self, screen):
        x_cor = self.width*self.index[1]
        y_cor = self.height*self.index[0]
        pygame.draw.rect(screen, self.color, (x_cor, y_cor, self.width, self.height))
        if self.text:
            font = pygame.font.Font('Arcade.ttf', int(self.width*0.6))
            text = font.render(self.text, True, (255,255,255))
            screen.blit(text, (self.index[1]*self.width + 10, self.index[0]*self.height + 10))

    def render_text(self,screen):
        if self.text:
            font = pygame.font.Font('Arcade.ttf', int(self.width*0.6))
            text = font.render(self.text, True, (255,255,255))
            screen.blit(text, (self.index[1]*self.width + 10, self.index[0]*self.height + 10))


def render_label(start_tile, end_tile, screen):
    font = pygame.font.Font('ARCADE.TTF', 10) # start/end font
    start_label = font.render('Start', True, (255,255,255))
    end_label = font.render('end', True, (255,255,255))
    screen.blit(start_label, start_tile.index)
    screen.blit(end_label, end_tile.index)


def main():
    #construction
    screen_width = 600
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Board")
    rows = 12
    columns = 12
    color1 = (255, 255, 255)
    color2 = (255, 0, 0)
    color3 = (0, 0, 255)
    color4 = (0, 255, 0)
    #grid construction
    newGrid = Grid(screen_height, screen_width, rows, columns)
    # tiles construction
    tile_matrix = [[Tiles(newGrid.grid_width, newGrid.grid_height, (i, j), color1, color2, color3, color4)
        for j in range(columns)] for i in range(rows)]



    makingWalls = False
    running = True
    while running:
        screen.fill((255, 255, 255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # get the clicked tiles
            if event.type == pygame.MOUSEBUTTONDOWN:
                makingWalls = True

            if event.type == pygame.MOUSEBUTTONUP:
                makingWalls = False
        
        # making walls
        if makingWalls:
            pos = pygame.mouse.get_pos()
            row_index, column_index = newGrid.clicked(pos) 
            wall_tile = tile_matrix[row_index][column_index]
            wall_tile.makeWall()

        # draw grid and tile
        for i in tile_matrix:
            for j in i:
                j.drawTile(screen)

        newGrid.drawGrid(screen)
        
        pygame.display.update()

# main()
pygame.quit()

