import pygame

clock = pygame.time.Clock()

def to_explore(tile, Tile_matrix, end_tile):
    index = tile.index
    size_matrix = (len(Tile_matrix), len(Tile_matrix[0]))
    # check all four tiles around
    to_check = [[index[0] - 1, index[1]], [index[0] , index[1] - 1],
                [index[0] + 1, index[1]], [index[0], index[1] + 1]]

    to_out = []
    for tiles in to_check:

        if tiles[0] in range(size_matrix[0]) and tiles[1] in range(size_matrix[1]):

            # if Tile_matrix[tiles[0]][tiles[1]] == end_tile:
            #     Tile_matrix[tiles[0]][tiles[1]].makeNewlyDiscovered(tile)
            #     end_tile.type = 'end'
            #     return [end_tile]

            if Tile_matrix[tiles[0]][tiles[1]].type not in ['start', 0] :  # empty--1; wall--0; explored--2
            #     Tile_matrix[tiles[0]][tiles[1]].makeNewlyDiscovered(tile)
                to_out.append(Tile_matrix[tiles[0]][tiles[1]])
            
    
    return to_out


def astar(Tile_matrix, start_tile, end_tile, screen, newGrid, menu_list):

    def heuristic_distance(tile, end_tile):
        # one tile is away is 1
        # Manhattan distance = Xd+Yd
        Xd = abs(end_tile.index[0] - tile.index[0])
        Yd = abs(end_tile.index[1] - tile.index[1])
        return Xd+Yd

    open_list = [start_tile]
    current_tile = start_tile
    closed_list = []         #g,h,f=g+h
    distance = {current_tile:[0,0,0]} # g is shortest distance from starting tile (so far possible)
    clock_speed = 2
    sp = 0 # speed parameter
    while current_tile!= end_tile:
        # choose current tile i.e. open tile with minimum h val
        current_tile = open_list[0]
        for opentile in open_list:
            if distance[opentile][2] < distance[current_tile][2] : # choose lowest h walue
                current_tile = opentile
        open_list.remove(current_tile)
        closed_list.append(current_tile)
        current_tile.makeExplored()

        # now add explorable tiles to open list
        neartiles = to_explore(current_tile, Tile_matrix, end_tile)

        # check if tile has been explored already
        # if not: add to open list
        # if yes: check g value from currently to past one
        # if past h was smaller i.e. this path was longer path to reach this tile so let it be
        # else change g, h and add to open
        # if in closed list moveon
        for neartile in neartiles:
            if neartile in closed_list:
                continue
            if neartile not in open_list:
                open_list.append(neartile)
                g = distance[current_tile][0] + 1
                h = heuristic_distance(neartile,end_tile)
                distance[neartile] = [g, h, g+h]
                neartile.makeNewlyDiscovered(current_tile)
                neartile.text = str(g+h)
                if neartile == end_tile:
                    neartile.type = 'end'
                    current_tile = end_tile
                    break


            if neartile in open_list:
                if distance[neartile][0] > distance[current_tile][0] + 1:
                    g = distance[current_tile][0] + 1
                    h = heuristic_distance(neartile,end_tile)
                    distance[neartile] = [g, h, g+h]
                    neartile.parent = current_tile
                    neartile.makeNewlyDiscovered(current_tile)
                    neartile.text = str(g+h)

         # clock.tick(clock_speed)   # speed of solving/animation
        sp+=1
        if sp != clock_speed: continue
        sp = 0
        # drawing/randering/updating
        draw_matrix(Tile_matrix, screen, newGrid)
        render_label(start_tile, screen)
        render_label(end_tile, screen)
        # display menu/buttons
        draw_menu(menu_list, screen)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            
            if pygame.mouse.get_pressed() == (1, 0, 0):
                pos = pygame.mouse.get_pos()
                if menu_list[0].ishovering(pos):
                    clock_speed+=2
                elif menu_list[1].ishovering(pos):
                    clock_speed-=2
            
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

def render_label(tile, screen):
    icon = pygame.image.load(tile.type+'.png') # start/end pic
    # label = font.render(tile.type, True, (255,255,255))
    cord = (tile.index[1]*tile.width + 10, tile.index[0]*tile.height + 10)
    screen.blit(icon, cord)

def draw_menu(menu_list, screen):
    for button_ in menu_list:
        button_.draw_button(screen)

