import pathlib
import random
import typing as tp
from copy import deepcopy

import pygame
from pygame.locals import *

Cell = tp.Tuple[int, int]
Cells = tp.List[int]
Grid = tp.List[Cells]


class GameOfLife:
    def __init__(
        self,
        size: tp.Tuple[int, int],
        randomize: bool = True,
        max_generations: tp.Optional[float] = float("inf"),
    ) -> None:
        # Размер клеточного поля
        self.cell_height, self.cell_width = size
        # Предыдущее поколение клеток
        self.prev_generation = self.create_grid()
        # Текущее поколение клеток
        self.curr_generation = self.create_grid(randomize=randomize)
        # Максимальное число поколений
        self.max_generations = max_generations
        # Текущее число поколений
        self.generations = 1

    def create_grid(self, randomize: bool = True) -> Grid:
        if not randomize:
            return [[0 for _ in range(self.cols)] for __ in range(self.rows)]
        else:
            return [[random.choice([0, 1]) for _ in range(self.cols)] for __ in range(self.rows)]

    def get_neighbours(self, cell: Cell) -> Cells:
        n = []
        if Cell[0] > 0:
            n.append(self.curr_generation[Cell[0] - 1][Cell[1]])
        if Cell[0] < self.rows - 1:
            n.append(self.curr_generation[Cell[0] + 1][Cell[1]])
        if Cell[1] > 0:
            n.append(self.curr_generation[Cell[0]][Cell[1] - 1])
        if Cell[1] < self.cols - 1:
            n.append(self.curr_generation[Cell[0]][Cell[1] + 1])
        if Cell[0] > 0 and Cell[1] > 0:
            n.append(self.curr_generation[Cell[0] - 1][Cell[1] - 1])
        if Cell[0] > 0 and Cell[1] < self.cols - 1:
            n.append(self.curr_generation[Cell[0] - 1][Cell[1] + 1])
        if Cell[0] < self.rows - 1 and Cell[1] > 0:
            n.append(self.curr_generation[Cell[0] + 1][Cell[1] - 1])
        if Cell[0] < self.rows - 1 and Cell[1] < self.cols - 1:
            n.append(self.curr_generation[Cell[0] + 1][Cell[1] + 1])
        return n

    def get_next_generation(self) -> Grid:
        grid = []
        for x in range(0, self.cell_height):
            col = []
            for y in range(0, self.cell_width):
                if (
                    sum(self.get_neighbours((x, y))) == 3
                    and self.curr_generation[x][y] == 0
                    or self.curr_generation[x][y] == 1
                    and (
                        sum(self.get_neighbours((x, y))) == 3
                        or sum(self.get_neighbours((x, y))) == 2
                    )
                ):
                    col.append(1)
                else:
                    col.append(0)
            grid.append(col)
        return grid

    def step(self) -> None:
        """
        Выполнить один шаг игры.
        """
        self.prev_generation = self.curr_generation
        self.curr_generation = self.get_next_generation()
        self.generations += 1

    @property
    def is_max_generations_exceeded(self) -> bool:
        """
        Не превысило ли текущее число поколений максимально допустимое.
        """
        if self.max_generations and self.generations >= self.max_generations:
            return True
        return False

    @property
    def is_changing(self) -> bool:
        """
        Изменилось ли состояние клеток с предыдущего шага.
        """
        if self.max_generations and self.generations >= self.max_generations:
            return True
        return False

    @staticmethod
    def from_file(filename: pathlib.Path) -> "GameOfLife":
        """
        Прочитать состояние клеток из указанного файла.
        """
        with open(filename) as fin:
            grid = [[int(cell) for cell in row.strip()] for row in fin]
        game = GameOfLife((len(grid), len(grid[0])))
        game.curr_generation = grid
        return game

    def save(self, filename: pathlib.Path) -> None:
        """
        Сохранить текущее состояние клеток в указанный файл.
        """
        with open(filename) as fin:
            for _, line in enumerate(self.curr_generation):
                for _, e in enumerate(line):
                    fin.write(str(e))
                fin.write("\n")


if __name__ == "__main__":
    life = GameOfLife.from_file(pathlib.Path("glider.txt"))
    steps = 4  # задает количество итераций
    for _ in range(steps):
        life.step()
