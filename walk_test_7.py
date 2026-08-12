# same as walk_test_6 but no animating

# compare a-values to 50% and 90% coverage
# fixed: 10x10 torus, 1000 max_steps

#import py5
import random
import numpy as np

class Experiment1:
    def __init__(self, a):
        self.a = a
        self.cols = 10
        self.rows = 10
        self.moves = [{"dx": 0, "dy": -1}, {"dx": 0, "dy": 1}, {"dx": -1, "dy": 0}, {"dx": 1, "dy": 0}]
        self.step_count = 0
        self.max_steps = 1000

        self.spacing = 50
        self.offset = self.spacing // 2

        self.x = self.cols // 2
        self.y = self.rows //2

        self.grid = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        self.grid[self.x][self.y] = 1


        # def setup():
        #     global cols, rows, spacing
        #     py5.size(cols * spacing, rows * spacing)
        #     py5.background(255,0,0)

        def walk():
            cols, rows, moves, step_count, max_steps, spacing, offset, x, y, grid = self.cols, self.rows, self.moves, self.step_count, self.max_steps, self.spacing, self.offset, self.x, self.y, self.grid
            possible_moves = []
            weights = []

            for move in moves:
                x_new = (x+move["dx"]) % cols
                y_new = (y+move["dy"]) % rows
                possible_moves.append(move)

                n = grid[x_new][y_new]

                weight = 1/(a**n)
                weights.append(weight)

            step = random.choices(possible_moves, weights=weights)[0]
            weights = []
            possible_moves = []
            x_new = (x + step["dx"]) % cols
            y_new = (y + step["dy"]) % rows
            grid[x_new][y_new] += 1
            print(x_new, y_new)

            # # print(x_new, y_new)
            # py5.stroke(0,255,0)
            # py5.stroke_weight(2)

            # # not going off the grid (torus)
            # if not(x_new == 0 and x == cols-1) and not(x_new == cols-1 and x == 0) and not(y_new == 0 and y == rows-1) and not(y_new == rows-1 and y == 0):
            #     py5.line(x*spacing+offset, y*spacing+offset, x_new*spacing+offset, y_new*spacing+offset)
            x = x_new
            y = y_new

            step_count += 1

            # for i in range(rows):
            #         for j in range(cols):
            #             py5.stroke(255)
            #             py5.stroke_weight(25)
            #             py5.point(i*spacing+offset, j*spacing+offset)
            #             py5.fill(0)
            #             text_size = 12
            #             py5.text_size(text_size)
            #             py5.text_align(py5.CENTER, py5.CENTER)
            #             visits = grid[i][j]
            #             py5.text(str(visits), i*spacing+offset, j*spacing+offset)

                # py5.no_loop()

        # py5.run_sketch()

        while self.step_count < self.max_steps:
            walk()

            all_visits = np.array(self.grid).flatten()
            if np.count_nonzero(all_visits) > (self.cols*self.rows)//2:
                print(f"step count to reach {50}% coverage:", self.step_count)
            all_visits = np.array(self.grid).flatten()
                     
            if self.step_count >= self.max_steps:
                print("total number of lily pads:", self.cols*self.rows)
                print("visited lily pads:", np.count_nonzero(all_visits))
                print("coverage:", np.count_nonzero(all_visits)/(self.cols*self.rows)*100,"%")
                print(self.grid)
        

a2 = Experiment1(2)
a5 = Experiment1(5)
a10 = Experiment1(10)
a100 = Experiment1(100)

# NEXT STEP: RESTRUCTURE WALK() CORRECTLY
# goal: create list of experiments and plan the class/functions structure for all of it
# can change as a i go but need overall structure

# possible plan:
# two types of weakly SAW: a^-n (exponential) and (n+1)^a

# compare (create graphs for, flesh out plan better on google doc):
# mean number of self-intersections
# number of distinct vertices created
# probability of returning to starting point
# variance of node visits when max_steps < (rows*col)
# quartiles, 10th-percentiles, other percentiles, histogram for visit counts
# how many steps it takes to visit every site
# run each experiment for 5-100 trials, average
# among these models, comparison in distribution for the number of visits between the nodes
# avoid last 10 nodes visited



