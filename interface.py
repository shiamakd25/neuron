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
            section.surface.blit(self.surface, (current_x, current_y))
