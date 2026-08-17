import py5
import numpy as np
import random
import matplotlib.pyplot as plt

class WeaklySelfAvoidingWalk:

    max_steps = 1000
    cols = 10
    rows = 10

    def __init__(self, weakener, a, spacing, animate):
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
        self.animate = animate

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
        
        self.grid[self.x][self.y] += 1
        possible_moves = []
        weights = []
        
        for move in self.moves:
            # traverse through 4 possible next lily pads
            # check weakener
            # decide next step based on weakener
            # how to make eraser allow backtracking?
            x_new = (self.x+move["dx"]) % cols
            y_new = (self.y+move["dy"]) % rows
            possible_moves.append(move)
            
            n = self.grid[x_new][y_new]
            
            match self.weakener:
                case "exponential":
                    print("exponential")
                    weights.append(1/(self.a**n))
                    
                case "polynomial":
                    print("polynomial")
                    weights.append(1/(n+1)**self.a)
                    
                case "eraser":
                    print("eraser") #make weight=0 if in last_a_nodes
                    if (x_new, y_new) in self.last_a_nodes_visited:
                        weights.append(0)
                    else:
                        weights.append(1)
                        
                    if not(1 in weights) and (x_new, y_new) == self.last_a_nodes_visited[-1]:
                        # go back to previous node if stuck (all surrounding weights 0)
                        weights.append(1)
                    
                    if len(self.last_a_nodes_visited) < self.a:
                        self.last_a_nodes_visited.pop(0)
            
        step = random.choice(possible_moves, weights = weights)[0]
        x_new = (self.x + step["dx"]) % cols
        y_new = (self.y + step["dy"]) % rows
        
        if self.weakener == "eraser":
            self.last_a_nodes_visited.append((x_new, y_new))
            
        self.x = x_new
        self.y = y_new
        self.grid[x_new][y_new]
        self.step_count += 1
        

        
    def full_walk(self):
        """
        call step() max_steps number of times
        animate if self.animate == True
        return a-value, node visits variance
        """
        global max_steps
        
        #how to make animation on/off
        
        for i in range(max_steps):
            self.step(self)
        
        all_visits = np.array(self.grid).flatten()
        variance = np.var(all_visits)
        print("total number of lily pads:", cols*rows)
        print("visited lily pads:", np.count_nonzero(all_visits))
        print("coverage:", np.count_nonzero(all_visits)/(cols*rows)*100,"%")
        print("variance:", variance)
        #print("quartiles:", np.percentile(all_visits,[25,50,75]))
        print("max:", np.max(all_visits))
        
        return self.a, variance
    
    def animation_switch(self):
        self.animate = not self.animate
        
class WSAWRunner:
    
    def __init__(self, weakener, a_values, spacing, animate):
        self.a_values = []
        self.variances = []
        self.weakener = weakener
        self.a_values = a_values
        self.spacing = spacing
        self.animate = animate
        

    def main_runner(self, num_trials, weakener):
        """
        set number of full walks per a-value
        create num_trials number of WSAW objects
        collect all num_trials number of variances (common a-value)
        average variances per a-value (avg the variances list for that a-value)
        
        take that avged_variance and append it to the list
        append the corresponding to the list a_values
        
        append that average variance to self.variances
        input: a-value, weakener
        """
        for i in range(num_trials):
            
        a_values = self.a_values
        variances = self.variances
        
        plt.plot(a_values, variances)
        plt.show()

    def get_avg_var_for_specific_a_value(self, specific_a_value):
        """
        need a-value
        need variance of node visits
        """
        my_wsaw = WeaklySelfAvoidingWalk(self.weakener, specific_a_value, self.animate)
        (a_value, variance) = WSAW_obj.full_walk()
        self.a_values.append(a_value)
        self.variances.append(variance)
        
        
if __name__ == "__main__":
    my_WSAWRunner = WSAWRunner()

    