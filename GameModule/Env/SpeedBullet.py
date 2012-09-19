#!/usr/bin/python2.7

import pygame

from GameModule.Config import *
from Bullet import Bullet

class SpeedBullet(Bullet):
  def __init__(self, x, y):
    super( SpeedBullet, self ).__init__()
    self.image = pygame.Surface( (15,15) )
    pygame.draw.polygon( self.image, (0,255,0), [ (0,0), (14,0), (7,14) ] )  
    self.image.set_colorkey( (0,0,0) )
    self.rect = self.image.get_rect()
    self.rect.centerx = x
    self.rect.centery = y

    self.bType = "enemy"

    self.hit = 5

  def update(self):
    self.rect.move_ip( 0, 5 )
    if self.rect.topleft[1] > config["screen_size"][1]:
      self.kill()

  def bulletType(self):
    return self.bType

