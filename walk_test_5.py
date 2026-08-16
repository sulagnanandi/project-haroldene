# 2D SRW with exponential weights

import py5
import random
import numpy as np

moves = [{"dx": 0, "dy": -1}, {"dx": 0, "dy": 1}, {"dx": -1, "dy": 0}, {"dx": 1, "dy": 0}]
step_count = 0
max_steps = 1000
a = 1.01 #pressure to share the wealth

cols = 10
rows = 10
spacing = 50
offset = spacing // 2

x = cols // 2
y = rows //2

grid = [[0 for _ in range(cols)] for _ in range(rows)]
grid[x][y] = 1

def setup():
    global cols, rows, spacing
    py5.size(cols * spacing, rows * spacing)
    py5.background(255,0,0)

def draw():
    global x, y, a, grid, step_count, max_steps, cols, rows, spacing
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

    # print(x_new, y_new)
    py5.stroke(0,255,0)
    py5.stroke_weight(2)

    # not going off the grid (torus)
    if not(x_new == 0 and x == cols-1) and not(x_new == cols-1 and x == 0) and not(y_new == 0 and y == rows-1) and not(y_new == rows-1 and y == 0):
        py5.line(x*spacing+offset, y*spacing+offset, x_new*spacing+offset, y_new*spacing+offset)
    x = x_new
    y = y_new

    step_count += 1

    for i in range(rows):
            for j in range(cols):
                py5.stroke(255)
                py5.stroke_weight(25)
                py5.point(i*spacing+offset, j*spacing+offset)
                py5.fill(0)
                text_size = 12
                py5.text_size(text_size)
                py5.text_align(py5.CENTER, py5.CENTER)
                visits = grid[i][j]
                py5.text(str(visits), i*spacing+offset, j*spacing+offset)

    if step_count >= max_steps:
        all_visits = np.array(grid).flatten()
        print("total number of lily pads:", cols*rows)
        print("visited lily pads:", np.count_nonzero(all_visits))
        print("coverage:", np.count_nonzero(all_visits)/(cols*rows)*100,"%")
        print("variance:", np.var(all_visits))
        #print("quartiles:", np.percentile(all_visits,[25,50,75]))
        print("max:", np.max(all_visits))
        py5.no_loop()

py5.run_sketch()