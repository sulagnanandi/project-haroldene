import py5

def setup():
    py5.size(400,400)
    print("we in setup gang")

def draw():
    py5.background(50)
    py5.circle(200,200,50)

py5.run_sketch()