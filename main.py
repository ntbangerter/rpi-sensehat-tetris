import random

import numpy as np


BOARD_SIZE = 8

class Shape:

    def __init__(self, shape, color):
        self.shape = np.array(shape)
        self.color = color

    def get_color(self):
        return self.color

    def get_shape(self):
        return self.shape

    def rotate_left(self):
        self.shape = np.rot90(self.shape)

    def rotate_right(self):
        self.shape = np.rot90(self.shape, 3)

    def get_put_positions(self, row, col):
        positions = []

        anchor = row * BOARD_SIZE + col

        for i, row in enumerate(self.shape):
            for j, value in enumerate(row):
                if value == 1:
                    position = 3 * (anchor + 8 * i + j)
                    positions.append(position)
                    positions.append(position + 1)
                    positions.append(position + 2)

        return positions


def create_shape(shape_switch=None):
    if shape_switch is None:
        shape_switch = random.randint(0, 5)

    if shape_switch == 0:
        shape = [[1, 0], [1, 1]]
        color = [64, 0, 0]

    elif shape_switch == 1:
        shape = [[1, 1, 1]]
        color = [0, 64, 0]

    elif shape_switch == 2:
        shape = [[1, 1], [1, 1]]
        color = [0, 0, 64]

    elif shape_switch == 3:
        shape = [[0, 1, 0], [1, 1, 1]]
        color = [64, 64, 0]

    elif shape_switch == 4:
        shape = [[1, 0, 0], [1, 1, 1]]
        color = [64, 0, 64]

    elif shape_switch == 5:
        shape = [[0, 0, 1], [1, 1, 1]]
        color = [0, 64, 64]


    return Shape(shape, color)


shape = Shape([[1, 0], [1, 1]], [64, 0, 0])

base = np.zeros((8, 8, 3))
base.put(shape.get_put_positions(3, 3), shape.get_color())

print(base)
