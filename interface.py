import pygame as pg


class Section:
    def __init__(self, width: float, height: float, index: int, parent):
        self.width_ratio: float = width
        self.height_ratio: float = height
        self.index: int = index
        self.parent = parent

    @property
    def width(self):
        return self.parent.width * self.width_ratio

    @property
    def height(self):
        return self.parent.height * self.height_ratio

    @property
    def surface(self):
        return pg.Surface((self.width, self.height))


class Container:
    def __init__(self, width: float, height: float, sections: list):
        self.width: float = width
        self.height: float = height
        self.sections: list = sections
