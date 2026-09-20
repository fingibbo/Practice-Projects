from abc import ABC, abstractmethod
import random

class Player(ABC):
    @abstractmethod
    def __init__(self) -> None:
        self.moves = []
        self.position = (0, 0)
        self.path = [self.position]

    def make_move(self) -> tuple:
        move = random.choice(self.moves)
        self.position = tuple(map(sum, zip(self.position, move)))
        self.path.append(tuple(self.position))
        return self.position

    @abstractmethod
    def level_up(self):
        pass

class Pawn(Player):
    def __init__(self) -> None:
        super().__init__()
        self.moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def level_up(self):
        self.moves = self.moves + [(1, 1), (1, -1), (-1, 1), (-1, -1)]
