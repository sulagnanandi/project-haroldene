print("HII UR CODE STARTED")
import py5
print("py5 imported")
import random
import numpy as np

step_count = 0
max_steps = 10000

#dictionary of moves: down, up, left, right
moves = [{"dx": 0, "dy": -1}, {"dx": 0, "dy": 1}, {"dx": -1, "dy": 0}, {"dx": 1, "dy": 0}]

#creating my global variables!!
spacing = 10

cols = 100
rows = 100

#haroldene's coordinates
x = 0
y = 0

#to keep track of lily pads haroldene has leaped onto/visited so far
grid = []

#change this to False if u wanna try 1/(n+1)
use_exponential = True

#a in 1/(a^n)
a = 2


def setup():
    global grid, x, y

    py5.size(cols*spacing, rows*spacing)

    print("we in setup gang") #testing testing testing ASLDKFJ

    #starting in middle so haroldene has room to leap around
    x = cols//2
    y = rows//2

    #initializing the grid with 0s (meaning no visits yet)
    grid = [[0 for j in range(rows)] for i in range(cols)]

    grid[x][y] += 1

    print("finished setup")



def draw():
    print("inside draw")

    global x,y,grid,step_count

    possible_moves=[] #gonna fill these with neighbouring lily pads

    weights=[] #how attractive each move is

    #go thru down, up, left, right
    for move in moves:

        #torus mode:
        #haroldene exits one side and reappears opposite side
        x_new=(x+move["dx"])%cols
        y_new=(y+move["dy"])%rows

        possible_moves.append(move)

        n=grid[x_new][y_new]

        #try 1/(a^n)
        if use_exponential:
            weight=1/(a**n)

        #try 1/(n+1)
        else:
            weight=1/(n+1)

        weights.append(weight)

    #weighted random instead of strict self avoiding
    step=random.choices(
        possible_moves,
        weights=weights,
        k=1
    )[0]

    x_new=(x+step["dx"])%cols
    y_new=(y+step["dy"])%rows

    #more visits = darker
    visits=grid[x_new][y_new]

    darkness=min(visits*20,255)

    py5.stroke(255-darkness)

    py5.stroke_weight(2)

    py5.line(
        x*spacing,
        y*spacing,
        x_new*spacing,
        y_new*spacing
    ) #line segment from current lily pad to new randomly-chosen lily pad

    x=x_new
    y=y_new

    grid[x][y]+=1 #mark visit count

    step_count += 1

    print(step_count)

    if step_count >= max_steps:

        all_visits=np.array(grid).flatten()

        print("mean:", np.mean(all_visits))
        print("variance:", np.var(all_visits))
        print("quartiles:", np.percentile(all_visits,[25,50,75]))
        print("max:", np.max(all_visits))
        print("visited:", np.count_nonzero(all_visits))
        print("coverage:", np.count_nonzero(all_visits)/(cols*rows)*100,"%")

        py5.no_loop()


if __name__ == "__main__":
    py5.run_sketch() #actually run the sketch