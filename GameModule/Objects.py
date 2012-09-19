#!/usr/bin/python2.7

from Env.BattleShip import *

import math
import pygame
from pygame.locals import *

class Objects:
  def __init__(self,status):
    self.enemies = pygame.sprite.Group()
    self.player = BattleShip(status)
    self.bullets = pygame.sprite.Group()
    self.powerups = pygame.sprite.Group()

  def updateEnemies(self):
    self.enemies.update()

  def updateBullets(self):
    self.bullets.update()

  def updatePowerups(self):
    self.powerups.update()

  def movePlayer( self, direction ):
    d = 1
    if direction == K_LEFT:
      d = -1
    self.player.move( math.copysign( 5, d ) )
