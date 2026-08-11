print("yoyoyo its ur boi rai panesar")
import py5
import random

#dictionary of moves: down, up, left, right
moves = [{"dx": 0, "dy": -1}, {"dx": 0, "dy": 1}, {"dx": -1, "dy": 0}, {"dx": 1, "dy": 0}]

#creating my global variables!!
spacing = 10

cols = 0
rows = 0

#haroldene's coordinates
x = 0
y = 0

#to keep track of lily pads haroldene has leaped onto/visited so far
grid = []

def is_valid(i,j):
    global cols, rows, grid #using global variables, not making diff local ones bc no need to

    #mfw haroldene tries to escape the pond :(
    if (i < 0 or i >= cols) or (j < 0 or j >= rows):
        return False
    
    #cell == 0 means we haven't visited the lily pad yet, so yay valid :D
    #cell == 1 means we have already visited the lily pad, so we're not going there again D:
    return grid[i][j] == 0

def setup():
    global cols, rows, grid, x, y #using global variables, not making diff local ones bc no need to

    py5.size(400,400)
    print("we in setup gang") #testing testing testing A;SLDKFJ

    #sort of setting up a ~40x40 tiles kinda thing
    cols = py5.width // spacing
    rows = py5.height // spacing

    #starting in middle so haroldene has room to leap around
    x = cols // 2
    y = rows // 2

    #initializing the grid with 0s (meaning we haven't visited any lily pads yet)
    grid = [[0 for j in range(rows)] for i in range(cols)]

    grid[x][y] = 1 #starting lily pad ofc visited, can change the acc starting point in global var setup at the top

def draw():
    global x, y, grid #trusty global vars again

    py5.stroke(255) #white lines to trace path

    py5.stroke_weight(spacing*0.25) #make thickness of lines dependent on spacing? idk test later ig

    py5.point(x*spacing, y*spacing) #mark haroldene's current lily pad coordinates by drawing a point

    possible_moves = [] #gonna fill these with the good-to-visit neighbouring lily pads

    #go thru down, up, left, right and see if those positions have been visited with is_valid
    for move in moves:

        #moving on the grid itself, NOT pixels
        x_new = x + move["dx"]
        y_new = y + move["dy"]

        if is_valid(x_new, y_new):
            possible_moves.append(move)
    
    #4 surrounding lily pads since its like a 2d grid kinda thing, so if there are any not visited ones (aka not stuck), randomly pick one to leap onto
    if len(possible_moves) > 0:

        step = random.choice(possible_moves) #randomly choose a valid move for haroldene to leap to

        x_new = x + step["dx"]
        y_new = y + step["dy"]

        py5.line(
            x*spacing,
            y*spacing,
            x_new*spacing,
            y_new*spacing
        ) #line segment from current lily pad to new randomly-chosen lily pad

        x = x_new #update haroldene's current coordinates to the new lily pad
        y = y_new

        grid[x][y] = 1 #mark the new lily pad as visited

    else:
        print("haroldene is stuck :(") #if there are no valid moves, haroldene is stuck and the walk is over
        py5.no_loop() #stop the draw loop since we're done with the walk
    
if __name__ == "__main__":
    py5.run_sketch() #actually run the sketch