import pygame

clock = pygame.time.Clock()

class stack():
    def __init__(self):
        self.node_list = []
    
    def empty(self):
        return self.node_list ==[]

    def remove(self):
        if self.empty():
            raise Exception("stack's empty")
        return self.node_list.pop()

    def add(self, tile):
        self.node_list.append(tile)

    def clearall(self):
        self.node_list.clear()

# Depth first search
def dfs(Tile_matrix, start_tile, end_tile, screen, newGrid):
    stack_dfs = stack()
    stack_dfs.add(start_tile)

    # solve the maze
    while not stack_dfs.empty():
        current_tile = stack_dfs.remove()
        to_explore(stack_dfs, current_tile, Tile_matrix, end_tile)
        current_tile.makeExplored()
        # drawing/randering/updating
        draw_matrix(Tile_matrix, screen, newGrid)

        clock.tick(2)   # speed of solving/animation
        render_label(start_tile, screen)
        render_label(end_tile, screen)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

    current_tile = end_tile
    path = []
    # give the path
    while current_tile.parent:
        path.append(current_tile.parent)
        current_tile.makepath()
        current_tile = current_tile.parent
        

def draw_matrix(tile_matrix, screen, newGrid) : 
    
    # draw grid and tile
    for i in tile_matrix:
        for j in i:
            j.drawTile(screen)
    newGrid.drawGrid(screen)


def to_explore(stack_dfs, tile, Tile_matrix, end_tile):
    index = tile.index
    size_matrix = (len(Tile_matrix), len(Tile_matrix[0]))
    # check all four tiles around
    to_check = [[index[0] - 1, index[1]], [index[0] , index[1] - 1],
                [index[0] + 1, index[1]], [index[0], index[1] + 1]]

    for tiles in to_check:

        if tiles[0] in range(size_matrix[0]) and tiles[1] in range(size_matrix[1]):

            if Tile_matrix[tiles[0]][tiles[1]].type == 1 :  # empty--1; wall--0; explored--2
                Tile_matrix[tiles[0]][tiles[1]].makeNewlyDiscovered(tile)
                stack_dfs.add(Tile_matrix[tiles[0]][tiles[1]])

            elif Tile_matrix[tiles[0]][tiles[1]] == end_tile:
                Tile_matrix[tiles[0]][tiles[1]].makeNewlyDiscovered(tile)
                end_tile.type = 'end'
                stack_dfs.clearall()
                return


def render_label(tile, screen):
    icon = pygame.image.load(tile.type+'.png') # start/end pic
    # label = font.render(tile.type, True, (255,255,255))
    cord = (tile.index[1]*tile.width + 10, tile.index[0]*tile.height + 10)
    screen.blit(icon, cord)
