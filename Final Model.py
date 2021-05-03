# -*- coding: utf-8 -*-
"""
Created on Sun May  2 10:27:26 2021

@author: z5490
"""
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.animation 
import random
import operator
import matplotlib.pyplot
import agentframework_new
import csv
import tkinter
import requests
import bs4

f = open("in.txt")
environment = []
for line in f:
    parsed_line = str.split(line,",")
    rowlist = []
    for word in parsed_line:
        rowlist.append(float(word))
    environment.append(rowlist)
    
r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
content = r.text
soup = bs4.BeautifulSoup(content, 'html.parser')
td_ys = soup.find_all(attrs={"class" : "y"})
td_xs = soup.find_all(attrs={"class" : "x"})
print(td_ys)
print(td_xs)

num_of_agents = 10
num_of_iterations = 100
neighbourhood = 20
agents = []


fig = matplotlib.pyplot.figure(figsize=(5, 5))
ax = fig.add_axes([0, 0, 1, 1])
carry_on = True	
#ax.set_autoscale_on(False)
for i in range(num_of_agents):
      y = int(td_ys[i].text)
      x = int(td_xs[i].text)
      agents.append(agentframework_new.Agent(environment, agents, y, x))

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
      print(agents[i].x, agents[i].y)
    matplotlib.pyplot.xlim(0, 99)
    matplotlib.pyplot.ylim(0, 99)
    matplotlib.pyplot.imshow(environment)

    
def gen_function(b = [0]):
    a = 0
    global carry_on #Not actually needed as we're not assigning, but clearer
    while (a < 10) & (carry_on) :
        yield a			# Returns control and waits next call.
        a = a + 1

def Run():
    animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
    canvas.draw()
    

root = tkinter.Tk() 
root.wm_title("Model")
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run model", command=Run) 

tkinter.mainloop()

