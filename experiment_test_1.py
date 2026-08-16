import py5
import numpy as np
import random

class WeaklySelfAvoidingWalk:

    max_steps = 1000
    cols = 10
    rows = 10

    def __init__(self, step_count, max_steps, weakener, spacing):
        global cols, rows
        self.grid = [[0 for _ in range(cols)] for _ in range(rows)]
        self.weakener = weakener
        self.spacing = spacing
        self.offset = spacing // 2

class WSAWRunner:

    def __init__(self):
        print("hi")

    def main_runner():
        print("hi")

    def one_full_walk():
        print("hi")

    