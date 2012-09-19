#!/usr/bin/python2.7

import pygame

class BattleObject( pygame.sprite.Sprite ):
  def __init__(self, maxHitpoints):
    super(BattleObject,self).__init__()
    self.hp = (maxHitpoints,maxHitpoints)

  def makeHit( self, hit ):
    (hpMax,hp) = self.hp
    self.hp = (hpMax,hp-hit)
    if self.hp[1] <= 0:
      self.destroyed = True
