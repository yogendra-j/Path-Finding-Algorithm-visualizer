from DFS import*

class Queue(stack):
    # overload remove method
    def remove(self):
        if self.empty():
            raise Exception("Queue's empty")
        return self.node_list.pop(0)

# Breadth first search
def bfs(Tile_matrix, start_tile, end_tile, screen, newGrid, menu_list):
    queue_bfs = Queue()
    queue_bfs.add(start_tile)
    clock_speed = 2

    # solve the maze
    while not queue_bfs.empty():
        current_tile = queue_bfs.remove()
        to_explore(queue_bfs, current_tile, Tile_matrix, end_tile)
        current_tile.makeExplored()
        # drawing/randering/updating
        draw_matrix(Tile_matrix, screen, newGrid)

        clock.tick(clock_speed)   # speed of solving/animation
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