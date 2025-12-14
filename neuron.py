import pygame as pg


class Neuron:
    def __init__(self, default_weight: float, default_bias: float, input: int):
        self.weight: float = default_weight
        self.bias: float = default_bias
        self.output = self.weight * input + self.bias
        self.error: float = 0
