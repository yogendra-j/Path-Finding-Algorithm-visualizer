# import Board
from Board import*
from DFS import*
from BFS import*
from menu import *
from Astar import *

pygame.init()

def render_label(tile, screen):
    icon = pygame.image.load(tile.type+'.png') # start/end pic
    # label = font.render(tile.type, True, (255,255,255))
    cord = (tile.index[1]*tile.width + 10, tile.index[0]*tile.height + 10)
    screen.blit(icon, cord)


def initialization():
    global  astar_button, newGrid, screen, status, another_mouse_input, dfs_button , grid_width,menu_width 
    global  tile_matrix, makingWalls, end_tile, start_tile, bfs_button, algo_name, de_clock_button, in_clock_button
    grid_width = 1000 
    menu_width = 150
    screen_width = grid_width + menu_width #for menu
    screen_height = 800
    # screen/window construction
    screen = pygame.display.set_mode((screen_width, screen_height))
    rows = 40
    columns = 40
    #colors
    white = (255, 255, 255)
    red = (255, 0, 0)
    blue = (0, 0, 255)
    green = (0, 255, 0)
    brown = (165,42,42)
    #grid construction
    newGrid = Grid(screen_height, grid_width, rows, columns)
    # tiles construction
    tile_matrix = [[Tiles(newGrid.grid_width, newGrid.grid_height, (i, j), white, red, blue, green)
        for j in range(columns)] for i in range(rows)]

    # loop initializing parameters
    start_tile = None
    end_tile = None
    another_mouse_input = False
    status = "yet to search"
    makingWalls = False
    algo_name = None
    # menu/buttons
    in_clock_button = Button((int(menu_width*0.8), int(screen_height*0.1)), brown, 
        (grid_width + int(0.1*menu_width), int(0.02*screen_height)), '+Speed')

    de_clock_button = Button((int(menu_width*0.8), int(screen_height*0.1)), brown, 
        (grid_width + int(0.1*menu_width), int(0.13*screen_height)), '-Speed')

    dfs_button = Button((int(menu_width*0.8), int(screen_height*0.1)), brown, 
        (grid_width + int(0.1*menu_width), int(0.24*screen_height)), 'DFS')

    bfs_button = Button((int(menu_width*0.8), int(screen_height*0.1)), brown, 
        (grid_width + int(0.1*menu_width), int(0.35*screen_height)), 'BFS')

    astar_button = Button((int(menu_width*0.8), int(screen_height*0.1)), brown, 
        (grid_width + int(0.1*menu_width), int(0.46*screen_height)), 'A*')

def main():
    global grid_width, newGrid, screen, makingWalls, end_tile, start_tile, dfs_button, astar_button, menu_width 
    global tile_matrix, status, another_mouse_input, bfs_button, menu_width, algo_name, de_clock_button, in_clock_button
    initialization()
    menu_list = [in_clock_button, de_clock_button, dfs_button, bfs_button, astar_button]
    running = True
    while running:
        screen.fill((255, 255, 255))

        # draw grid and tile
        for i in tile_matrix:
            for j in i:
                j.drawTile(screen)
        # draw grid 
        newGrid.drawGrid(screen)
        # get events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # get the clicked tiles
            if pygame.mouse.get_pressed() == (1, 0, 0):
                pos = pygame.mouse.get_pos()
                if pos[0] <= grid_width:
                    makingWalls = True

            if pygame.mouse.get_pressed() == (0, 0, 1) and not start_tile:
                pos = pygame.mouse.get_pos()
                if pos[0] <= grid_width:
                    startRow, startColumn = newGrid.clicked(pos)
                    start_tile = tile_matrix[startRow][startColumn]
                    start_tile.makeStartEnd('start')

            if pygame.mouse.get_pressed() == (0, 0, 1) and another_mouse_input:
                pos = pygame.mouse.get_pos()
                if pos[0] <= grid_width:
                    endRow, endColumn = newGrid.clicked(pos)
                    end_tile = tile_matrix[endRow][endColumn]
                    end_tile.makeStartEnd('end')

            if event.type == pygame.MOUSEBUTTONUP:
                if pos[0] <= grid_width:
                    if event.button == 1:
                        makingWalls = False
                    if event.button == 3:
                        another_mouse_input = True

            # select algo_name with buttons
            if pygame.mouse.get_pressed() == (1, 0, 0):
                pos = pygame.mouse.get_pos()
                if dfs_button.ishovering(pos):
                    algo_name = 'dfs'
                elif bfs_button.ishovering(pos):
                    algo_name = 'bfs'
                elif astar_button.ishovering(pos):
                    algo_name = 'A*'

            # re-initialize the boad
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    initialization()

        # making walls
        if makingWalls:
            pos = pygame.mouse.get_pos()
            rowWall, columnWall = newGrid.clicked(pos) 
            try:
                wall_tile = tile_matrix[rowWall][columnWall]
                wall_tile.makeWall()
            except :
                makingWalls = False

        if end_tile and status == "yet to search":
            render_label(end_tile, screen)
            # select which algo to use with buttons
            if algo_name == 'bfs':
                bfs(tile_matrix, start_tile, end_tile, screen, newGrid, menu_list)
                status = "done searching"
            elif algo_name == 'dfs':
                dfs(tile_matrix, start_tile, end_tile, screen, newGrid, menu_list)
                status = "done searching"
            elif algo_name == 'A*':
                astar(tile_matrix, start_tile, end_tile, screen, newGrid, menu_list)
                status = "done searching"
            

        # blit start/end icons
        if start_tile :
            render_label(start_tile, screen)
        if end_tile:
            render_label(end_tile, screen)
        
        # display menu/buttons
        for button_ in menu_list:
                button_.draw_button(screen)
        # update screen
        pygame.display.update()

main()
pygame.quit()