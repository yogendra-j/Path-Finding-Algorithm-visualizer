from menu import*
def make_menu(menu_width, screen_height, grid_width, ):
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

def draw_menu(screen):
    # display menu/buttons
    in_clock_button.draw_button(screen)
    de_clock_button.draw_button(screen)
    dfs_button.draw_button(screen)
    bfs_button.draw_button(screen)
    astar_button.draw_button(screen)
