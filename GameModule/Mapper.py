#!/usr/bin/python2.7

import json
from GameModule.Env import *

class Mapper:
  def __init__( self, objects ):
    self.objects = objects
    self.actualPass = 0
    self.maxPass = 0
    self.data = None

  def load( self, fileName ):
    self.data = json.load( open( 'Resources/map.data' ) )
    self.maxPass = len(self.data)
  
    for bit_ in self.data[self.actualPass]:
      print bit_
      name,x,y = bit_[0], bit_[1], bit_[2]
      self.parse( name, x, y )

  def nextStage(self):
    self.actualPass += 1
    if self.actualPass == self.maxPass:
      return False
    else:
      for bit_ in self.data[self.actualPass]:
        name,x,y = bit_[0], bit_[1], bit_[2]
        self.parse( name, x, y )
      return True

  def parse( self, name, x, y ):
    if name == "insect":
      EnemyInsect( x, y, self.objects.bullets ).add(self.objects.enemies)
    elif name == "biginsect":
      EnemyBigInsect( x, y, self.objects.bullets ).add(self.objects.enemies)
    elif name == "speedinsect":
      EnemySpeedInsect( x, y, self.objects.bullets ).add(self.objects.enemies)
