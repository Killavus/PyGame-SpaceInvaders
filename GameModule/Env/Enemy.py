#!/usr/bin/python2.7

from BattleObject import BattleObject

import pygame
import math

class Enemy( BattleObject ):
  def __init__(self, maxHitpoints):
    super( Enemy, self ).__init__(maxHitpoints)
    
    self.direction = 1

  def setDirection(self):
    self.direction *= -1

  def move(self, x):
    self.rect.move_ip( math.copysign( x, self.direction ), 0 )

  def drawHP(self):
    if self.spawnFrames > 0:
      return

    (iw,ih) = self.image.get_size()
  
    (bw,bh) = math.floor(iw*0.5),5
    pygame.draw.rect( self.image, (0,0,0), pygame.Rect( (iw/2-bw/2,0), (bw,bh) ) )
    
    if self.destroyed == True:
      return

    (maxHP,actualHP) = self.hp
    hpBarPercent = float(actualHP)/maxHP

    barColor = (0,255,0)
    if hpBarPercent < .50:
      barColor = (245,184,0)
    if hpBarPercent < .25:
      barColor = (255,0,0)

    pygame.draw.rect( self.image, barColor, pygame.Rect( (iw/2-bw/2+1,1), (math.floor((bw-2)*(hpBarPercent)), bh-2) ) )
