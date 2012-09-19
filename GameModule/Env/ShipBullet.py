#!/usr/bin/python2.7

import pygame
from Bullet import Bullet
from GameModule.Constants import *

class ShipBullet(Bullet):
  def __init__(self,x,y):
    super( ShipBullet, self ).__init__()
    self.image = pygame.Surface( (5,20) )
    self.image.fill( (255,0,0) )

    self.rect = self.image.get_rect()
    self.rect.centerx = x
    self.rect.centery = y
    self.bType = "player"

    self.hit = 20

  def update(self):
    self.rect.move_ip( 0, -3 )
    if self.rect.bottomleft[0] < 0:
      self.kill()


  def bulletType(self):
    return self.bType
