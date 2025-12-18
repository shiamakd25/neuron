import pygame as pg
import random


class Section:
    def __init__(self, width: float, height: float, index: int, parent):
        self.index: int = index
        self.parent = parent
        self.width = int(width * self.parent.width)
        self.height = int(height * self.parent.height)
        self.surface = pg.Surface((self.width, self.height))


class Container:
    def __init__(
        self,
        width: float,
        height: float,
        sections: list[Section],
        rows: int,
        columns: int,
    ):
        self.width: float = width
        self.height: float = height
        self.sections: list[Section] = sections
        self.rows: int = rows
        self.columns: int = columns
        self.surface = pg.Surface((self.width, self.height))

    def draw_sections(self):
        sections: list[Section] = self.sections
        last_section: Section = None
        current_x = 0
        current_y = 0

        for section in sections:
            if last_section:
                current_x += last_section.width
            if current_x >= self.width:
                current_x = 0
                current_y += last_section.height
            self.surface.blit(section.surface, (current_x, current_y))
            last_section = section
