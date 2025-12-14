import pygame as pg
from globals import *

pg.init()

window = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pg.display.set_caption("Neuron Simulation")

run = True

while run:
    window.fill(BLACK)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    pg.display.flip()

pg.quit()
