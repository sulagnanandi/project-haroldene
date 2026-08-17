import py5
import numpy as np
import random
import matplotlib.pyplot as plt

class WeaklySelfAvoidingWalk:

    max_steps = 1000
    cols = 10
    rows = 10

    def __init__(self, weakener, a, spacing):
        global cols, rows
        self.grid = [[0 for _ in range(cols)] for _ in range(rows)]
        self.moves = [{"dx":1, "dy":0}, {"dx":-1, "dy":0}, {"dx":0, "dy":1}, {"dx":0, "dy":-1}]
        self.weakener = weakener
        self.x = cols // 2
        self.y = rows // 2
        if weakener == "eraser":
            self.last_a_nodes_visited = [(self.x, self.y)]
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
        possible_moves = []
        weights = []
        
        for move in self.moves:
            # traverse through 4 possible next lily pads
            # attach weights based on weakener and a-value
            x_new = (self.x+move["dx"]) % cols
            y_new = (self.y+move["dy"]) % rows
            possible_moves.append(move)
            
            n = self.grid[x_new][y_new]
            
            
    
        self.step_count += 1
        self.grid[self.x][self.y] += 1
        
        
    def full_walk(self):
        """
        call step() max_steps number of times
        animate if self.animate == True
        return a-value, node visits variance
        """
        
    
    def animation_switch(self):
        if self.animate:
            self.animate = False
        else:
            self.animate = True
        
class WSAWRunner:
    
    def __init__(self):
        self.a_values
        self.variances

    def main_runner(self, num_trials):
        """
        set number of full walks per a-value
        input: a-value, weakener
        """
        for i in range(num_trials):
            a_values = self.a_values
            variances = self.variances
        
        plt.plot(a_values, variances)
        plt.show()

    def one_full_walk(WSAW_obj):
        """
        need a-value
        need variance of node visits
        """
        WSAW_obj.full_walk()
        


    