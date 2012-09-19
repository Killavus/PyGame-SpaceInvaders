#!/usr/bin/python2.7

from Constants import *
from Config    import *
class Status:
  def __init__(self):
    self.state = constants["state"]["ingame"]
    self.points = 0
    self.lives = config["lives"]
    self.enemiesRemaining = 0
  
  def setState(self,state):
    self.state = constants["state"][state]

  def getState(self):
    return self.state

