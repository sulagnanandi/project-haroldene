# very similar to walk_test_3.py but no py5 (no animation)

import random
import numpy as np
step_count = 0
max_steps = 1000


moves = [
    {"dx":0, "dy":-1}, 
    {"dx":0, "dy":1}, 
    {"dx":-1, "dy":0}, 
    {"dx":1, "dy":0}]

spacing = 10
cols = 100
rows = 100

x = 0
y = 0

grid = []

weight_functions = ["exponential", "rational"]

weight_function_choice = input("choose weight function (exponential or rational): ")
a = input("choose a value for a (only used for exponential):")

def starting_stuff():
    global grid, x, y
    print("haroldene is starting her walk")

    #start haroldene in centre
    x = cols//2 
    y = rows//2

    #initialize grid with 0s
    #structure is i think smth like going through each row (inner loop) and going through the rows (outer loop) and filling each cell with 0
    grid = [[0 for j in range(rows)] for i in range(cols)]

    grid[x][y] += 1

def walk():
    # print("inside walk function")

    global x,y,grid,step_count

    possible_moves=[] #will populate this with neighbouring lily pads (ones we are allowed to visit)
    weights=[] #how attractive each move is

    #go through down, up, left, right
    for move in moves:
        """
        go through the 4 move options
        make the new coordinate the og coordinate + the particular move we're on's dx and dy
        but also mod by the number of columns so we can wrap around
        check later: what if the new coordinate is negative? will it wrap around to the other side? i think so but check later
        """
        x_new = (x+move["dx"]) % cols
        y_new = (y+move["dy"]) % rows

        possible_moves.append((x_new, y_new))

        n = grid[x_new][y_new]

        if weight_function_choice == "exponential":
            weight = 1/(float(a)**n)
        else:
            weight = 1/(n**float(a)+1)

        weights.append(weight)

    step = random.choices(possible_moves, weights = weights, k=1)[0]

    x_new = (x+step[0]) % cols
    y_new = (y+step[1]) % rows

    visits = grid[x_new][y_new]

    x = x_new
    y = y_new

    grid[x][y] += 1

    step_count += 1

    print(step_count, x, y, visits)

    if step_count >= max_steps:

        all_visits = np.array(grid).flatten()

        print("mean:", np.mean(all_visits))
        print("variance:", np.var(all_visits))
        print("quartiles:", np.percentile(all_visits, [25, 50, 75]))
        print("max:", np.max(all_visits))
        print("visited:", np.count_nonzero(all_visits))
        print("coverage:", np.count_nonzero(all_visits)/(cols*rows)*100, "%")

        print("grid:")
        for row in grid:
            print(row)


def main():
    starting_stuff()

    while step_count < max_steps:
        walk()

if __name__ == "__main__":
    main()


        