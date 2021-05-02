# -*- coding: utf-8 -*-
"""
Created on Sun May  2 10:47:35 2021

@author: z5490
"""

import random
class Agent():
      def __init__(self,environment,agents,y,x):
        self.x = x
        self.y = y
        self.environment=environment
        self.store = 0
        self.agents=agents
        if (x == None):
             self._x = random.randint(0,100)
        else:
             self._x = x
        
      def move(self):
          if random.random() < 0.5:
            self.x = (self.x + 1) % 100
          else:
            self.x = (self.x - 1) % 100
          if random.random() < 0.5:
            self.y = (self.y + 1) % 100
          else:
            self.y = (self.y - 1) % 100
            
      def eat(self): # can you make it eat what is left?
          if self.environment[self.y][self.x] > 10:
              self.environment[self.y][self.x] -= 10
              self.store += 10
      
      def share_with_neighbours(self, neighbourhood):
       for agent in self.agents:
           dist = self.distance_between(agent) 
           if dist <= neighbourhood:
               sum = self.store + agent.store
               ave = sum /2
               self.store = ave
               agent.store = ave
               print("sharing " + str(dist) + " " + str(ave))

            
      def distance_between(self, agent):
           return (((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5