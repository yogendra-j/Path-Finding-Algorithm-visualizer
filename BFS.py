from DFS import*

class Queue():
    '''implimented with circular array '''
    def __init__(self):
        self.data = [None]*100
        self.size = 0
        self.first = 0

    def empty(self):
        return self.size == 0
    
    def add(self, tile):
        if self.size == len(self.data):
            self.resize(2*len(self.data))
        first_avail = (self.first + self.size)%len(self.data)
        self.data[first_avail] = tile
        self.size+=1

    def resize(self, new_length):
        old = self.data
        self.data = [None]*new_length
        for i in range(self.size):
            self.data[i] = old[(self.first + i)%len(old)]
        self.first = 0

    def remove(self):
        if self.empty():
            raise Exception("Queue's empty")
        tile_out = self.data[self.first]
        self.data[self.first] = None
        self.first = (self.first + 1)%len(self.data)
        self.size-=1
        return tile_out

    def clearall(self):
        self.data.clear()
        self.size = 0

# Breadth first search
def bfs(Tile_matrix, start_tile, end_tile, screen, newGrid, menu_list):
    queue_bfs = Queue()
    queue_bfs.add(start_tile)
    clock_speed = 2
    sp = 0  # speed parameter
    # solve the maze
    while not queue_bfs.empty():
        current_tile = queue_bfs.remove()
        to_explore(queue_bfs, current_tile, Tile_matrix, end_tile)
        current_tile.makeExplored()
        # clock.tick(clock_speed)   # speed of solving/animation
        sp+=1
        if sp != clock_speed: continue
        # drawing/randering/updating
        sp = 0
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