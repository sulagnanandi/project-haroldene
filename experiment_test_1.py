import py5
import numpy as np
import random
import matplotlib

class WeaklySelfAvoidingWalk:

    max_steps = 1000
    cols = 10
    rows = 10

    def __init__(self, weakener, a, spacing):
        global cols, rows
        self.grid = [[0 for _ in range(cols)] for _ in range(rows)]
        self.moves = [{"dx":1, "dy":0}, {"dx":-1, "dy":0}, {"dx":0, "dy":1}, {"dx":0, "dy":-1}]
        self.weakener = weakener
        self.spacing = spacing
        self.offset = spacing // 2
        self.step_count = 0
        self.animate = True

    def step(self):
        """
        go through 4 adjacent nodes
        weight of going to node base