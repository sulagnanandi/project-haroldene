import py5

def setup():
    py5.size(500,500)
    py5.background(255)
    py5.no_loop()

def draw():
    py5.fill(0,255,0)
    py5.rect(100,100,300,300)

py5.run_sketch()