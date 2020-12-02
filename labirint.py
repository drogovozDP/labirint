import pygame
import random

PINK = (255, 0, 155)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
BROWN = (234, 34, 32)


class Labirint():
    def __init__(self, screen):
        self.screen = screen
        self.cell_size = 5
        self.rows = int(pygame.display.Info().current_h / self.cell_size)
        self.cols = int(pygame.display.Info().current_w / self.cell_size)
        self.point = {'row': int(self.rows / 2), 'col': int(self.cols / 2)}
        self.stack = [{'row': int(self.rows / 2), 'col': int(self.cols / 2)}]
        self.map = self.create_map()

    def step(self):
        y = self.point['row']
        x = self.point['col']
        ways = []
        self.map[y][x].visited = True
        if x - 1 >= 0:
            if self.map[y][x - 1].visited == False:
                ways.append('Left')
        if x + 1 < self.cols:
            if self.map[y][x + 1].visited == False:
                ways.append('Right')
        if y - 1 >= 0:
            if self.map[y - 1][x].visited == False:
                ways.append('Top')
        if y + 1 < self.rows:
            if self.map[y + 1][x].visited == False:
                ways.append('Bottom')
        if len(ways) != 0:
            randWay = random.randint(0, len(ways) - 1)
        else:
            if len(self.stack) != 0:
                self.point = self.stack[-1]
                self.stack.pop()
            return
        a = {'row': 0, 'col': 0}
        a['row'] = self.point['row']
        a['col'] = self.point['col']
        self.stack.append(a)
        # print(ways)
        if ways[randWay] == 'Left':
            self.map[y][x].break_wall('Left')
            self.map[y][x - 1].break_wall('Right')
            self.point['col'] -= 1

        if ways[randWay] == 'Right':
            self.map[y][x].break_wall('Right')
            self.map[y][x + 1].break_wall('Left')
            self.point['col'] += 1

        if ways[randWay] == 'Top':
            self.map[y][x].break_wall('Top')
            self.map[y - 1][x].break_wall('Bottom')
            self.point['row'] -= 1

        if ways[randWay] == 'Bottom':
            self.map[y][x].break_wall('Bottom')
            self.map[y + 1][x].break_wall('Top')
            self.point['row'] += 1

    def create_map(self):
        map = []
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                pos_x = j * self.cell_size + self.cell_size / 2
                pos_y = i * self.cell_size + self.cell_size / 2
                row.append(Cell(pos_x, pos_y, self.screen, self.cell_size))
            map.append(row)
        return map

    def draw(self):
        for i in range(len(self.map)):
            for j in range(len(self.map[i])):
                self.map[i][j].draw()

        constSize =  + self.cell_size * 0.1
        pos_x = self.point['col'] * self.cell_size + constSize# draw where we are now
        pos_y = self.point['row'] * self.cell_size + constSize
        pygame.draw.rect(self.screen, GREEN, (pos_x , pos_y, self.cell_size - constSize * 2, self.cell_size - constSize * 2))

class Cell():
    def __init__(self, x, y, screen, cell_size):
        self.visited = False
        self.x = x - cell_size / 2
        self.y = y - cell_size / 2
        self.width = cell_size
        self.height = cell_size
        self.screen = screen
        self.walls = {'Left': True, 'Right': True, 'Top': True, 'Bottom': True}

    def break_wall(self, wall):
        self.walls[wall] = False

    def draw(self):
        color = PINK
        if self.visited:
            color = BLACK
        pygame.draw.rect(self.screen, color, (self.x, self.y, self.width, self.height))
        if self.walls['Left']:
            pygame.draw.line(self.screen, BROWN, [self.x, self.y], [self.x, self.y + self.height])
        if self.walls['Right']:
            pygame.draw.line(self.screen, BROWN, [self.x + self.width, self.y], [self.x + self.width, self.y + self.height])
        if self.walls['Top']:
            pygame.draw.line(self.screen, BROWN, [self.x, self.y], [self.x + self.width, self.y])
        if self.walls['Bottom']:
            pygame.draw.line(self.screen, BROWN, [self.x, self.y + self.height], [self.x + self.width, self.y + self.height])
