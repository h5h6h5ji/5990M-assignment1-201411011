# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 10:25:24 2021

@author: z5490
"""

import random
import operator
import matplotlib.pyplot
import agentframework
import csv

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

# Make the agents.
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment,agents))

for j in range(num_of_iterations):
    for i in range(num_of_agents):
        agents[i].move()
        agents[i].eat()
        agents[i].share_with_neighbours(neighbourhood)

matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.imshow(environment)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i].x, agents[i].y)
matplotlib.pyplot.show()

