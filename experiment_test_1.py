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
        weight of going to node based on weakener and a-value
        use grid to check n (num of node visits)
        ex: weight = a**-n
        select randomly out of the 4 with given weights
        grid[x_new][y_new] += 1
        x = x_new, y = y_new
        step_count += 1
        """
        
        self.step_count += 1

    def walk(self):
        """
        call step() max_steps number of times
        animate if self.animate == True
        return a-value, node visits variance
        """
        
        print("hi")
    
    def animation_switch(self):
        if self.animate:
            self.animate = False
        else:
            self.animate = True
        
class WSAWRunner:

    def __init__(self):
        print("hi")

    def main_runner():
        """
        set number of full walks per a-value
        input: a-value, weakener
        """
        
        print("hi")

    def one_full_walk():
        """
        need a-value
        need variance of node visits
        """
        
        print("hi")

    