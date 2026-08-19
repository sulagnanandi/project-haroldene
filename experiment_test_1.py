# import py5
import numpy as np
import random
import matplotlib.pyplot as plt

class WeaklySelfAvoidingWalk:

    def __init__(self, weakener, a):
        self.moves = [{"dx":1, "dy":0}, {"dx":-1, "dy":0}, {"dx":0, "dy":1}, {"dx":0, "dy":-1}]
        self.a = a
        self.weakener = weakener
        self.max_steps = 1000
        self.cols = 10
        self.rows = 10
        self.x = self.cols // 2
        self.y = self.rows // 2
        self.grid = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        # self.spacing = 50
        # self.offset = self.spacing // 2
        if weakener == "eraser":
            self.last_a_nodes_visited = [(self.x, self.y)]
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
        
        self.grid[self.x][self.y] += 1
        possible_moves = []
        weights = []
        
        for move in self.moves:
            # traverse through 4 possible next lily pads
            # check weakener
            # decide next step based on weakener
            # how to make eraser allow backtracking?
            x_new = (self.x+move["dx"]) % self.cols
            y_new = (self.y+move["dy"]) % self.rows
            possible_moves.append(move)
            
            n = self.grid[x_new][y_new]
            
            match self.weakener:
                case "exponential":
                    # print("exponential")
                    weights.append(1/(self.a**n))
                    
                case "polynomial":
                    # print("polynomial")
                    weights.append(1/(n+1)**self.a)
                    
                case "eraser":
                    # print("eraser") #make weight=0 if in last_a_nodes
                    if (x_new, y_new) in self.last_a_nodes_visited:
                        weights.append(0)
                    else:
                        weights.append(1)
                        
                    if not(1 in weights) and (x_new, y_new) == self.last_a_nodes_visited[-1]:
                        # go back to previous node if stuck (all surrounding weights 0)
                        weights.append(1)
                    
                    if len(self.last_a_nodes_visited) > self.a:
                        self.last_a_nodes_visited.pop(0)
            
        step = random.choices(possible_moves, weights=weights)[0]
        x_new = (self.x + step["dx"]) % self.cols
        y_new = (self.y + step["dy"]) % self.rows
        
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
        
        #how to make animation on/off
        
        for i in range(self.max_steps):
            self.step()
        
        all_visits = np.array(self.grid).flatten()
        variance = np.var(all_visits)
        print("total number of lily pads:", self.cols*self.rows)
        print("visited lily pads:", np.count_nonzero(all_visits))
        print("coverage:", np.count_nonzero(all_visits)/(self.cols*self.rows)*100,"%")
        print("variance:", variance)
        #print("quartiles:", np.percentile(all_visits,[25,50,75]))
        print("in:", np.min(all_visits))
        print("max:", np.max(all_visits))
        
        return variance
    
    #animate ts later
    """
    def setup(self):
        global self.cols, self.rows
        py5.size(self.cols * self.spacing, self.rows * self.spacing)
        py5.background(255,0,0)
       
    def animation_switch(self):
        self.animate = not self.animate
        if self.animate:
            py5.loop()
        else:
            py5.no_loop()
    """    
        
class WSAWRunner:
    
    def __init__(self, num_trials, weakener, a_values):
        self.num_trials = num_trials
        self.weakener = weakener
        self.a_values = a_values
        self.variances = []
        

    def main_runner(self):
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
        
        num_a_values = len(self.a_values)
        for i in range(num_a_values):
            # call get_avg_var_for_specific_a_value num_trials times
            a = self.a_values[i]
            var = self.get_avg_var_for_specific_a_value(a)
            self.variances.append(var)
            
        a_values = self.a_values
        variances = self.variances
        
        print(a_values)
        print(variances)
        
        plt.scatter(a_values, variances, s=5)
        plt.xlabel("a-values for "+self.weakener)
        plt.ylabel("variances")
        plt.show()

    def get_avg_var_for_specific_a_value(self, specific_a_value):
        """
        need a-value
        need variance of node visits
        """
        
        vars_over_specific_a_value = []
        
        for i in range(self.num_trials):
            my_wsaw = WeaklySelfAvoidingWalk(self.weakener, specific_a_value)
            var = my_wsaw.full_walk()
            vars_over_specific_a_value.append(var)
        
        avg_var_for_specific_a_value = np.average(vars_over_specific_a_value)
        return avg_var_for_specific_a_value
    
    def get_avg_var_for_specific_a_value(self, specific_a_value):
            """
            need a-value
            need variance of node visits
            """
            
            vars_over_specific_a_value = []
            
            for i in range(self.num_trials):
                my_wsaw = WeaklySelfAvoidingWalk(self.weakener, specific_a_value)
                var = my_wsaw.full_walk()
                vars_over_specific_a_value.append(var)
            
            avg_var_for_specific_a_value = np.average(vars_over_specific_a_value)
            return avg_var_for_specific_a_value

if __name__ == "__main__":
    
    num_trials_input = 100
    
    weakener_input = "exponential"
    a_values_input = [3, 2, 1.9, 1.75, 1.5, 1.25, 1.1, 1.01, 1]
    
    """
    weakener_input = "polynomial"
    a_values_input = [3, 2, 1.9, 1.75, 1.5, 1.25, 1.1, 1.01, 1, 0.9, 0.75, 0.5, 0.25, 0.1, 0.01]
    """
    
    """
    weakener_input = "eraser"
    a_values_input = [2,3,4,5]
    """
    
    # use print statements to make sure each version (esp eraser) calculating weights correctly
    # next: save graphs in a folder
    # next: what else to graph?
    
    # coverage time vs a-value --> THIS NEXT
    # quartiles vs a-value
    
    # final position after 1000 (or smaller, 10, 20) steps
    # run this a large number of times
    # is 1000 steps enough to get to a uniform random spot on the grid
    # with each of the three WSAW regimes
    # exponential, polynomial, eraser
    
    # document on what i did this summer
    
    my_WSAWRunner = WSAWRunner(num_trials_input, weakener_input, a_values_input)
    my_WSAWRunner.main_runner()