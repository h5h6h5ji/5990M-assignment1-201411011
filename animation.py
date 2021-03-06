# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 11:54:28 2021

@author: z5490
"""

import random
import operator
import matplotlib.pyplot
import agentframework
import csv
import matplotlib.animation 

f = open("in.txt")
environment = []
for line in f:
    parsed_line = str.split(line,",")
    rowlist = []
    for word in parsed_line:
        rowlist.append(float(word))
    environment.append(rowlist)
    

num_of_agents = 10
num_of_iterations = 100
neighbourhood = 20
agents = []


fig = matplotlib.pyplot.figure(figsize=(5, 5))
ax = fig.add_axes([0, 0, 1, 1])
carry_on = True	
#ax.set_autoscale_on(False)

# Make the agents.
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment,agents))

def update(frame_number):
    
    fig.clear()  
    global carry_on
    
    for j in range(num_of_iterations):
        for i in range(num_of_agents):
            agents[i].move()
            agents[i].eat()
            agents[i].share_with_neighbours(neighbourhood)
            
    for i in range(num_of_agents):
      matplotlib.pyplot.scatter(agents[i].x, agents[i].y)
      print(agents[i].x,agents[i].y)

    matplotlib.pyplot.xlim(0, 99)
    matplotlib.pyplot.ylim(0, 99)
    matplotlib.pyplot.imshow(environment)
    
def gen_function(b = [0]):
    a = 0
    global carry_on #Not actually needed as we're not assigning, but clearer
    while (a < 10) & (carry_on) :
        yield a			# Returns control and waits next call.
        a = a + 1
        
animation = matplotlib.animation.FuncAnimation(fig, update, interval=1, repeat=False, frames=gen_function)
matplotlib.pyplot.show()

