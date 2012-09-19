#!/usr/bin/python2.7

import pygame

from GameModule.Config import *
from Bullet import Bullet

class BigInsectBullet(Bullet):
  def __init__(self, x, y):
    super( BigInsectBullet, self ).__init__()
    self.image = pygame.Surface( (20,20) )
    pygame.draw.circle( self.image, (255,0,0), (10,10), 9 ) 
    self.image.set_colorkey( self.image.get_at( (0,0) ) )
    self.rect = self.image.get_rect()
    self.rect.centerx = x
    self.rect.centery = y

    self.bType = "enemy"

    self.hit = 50

  def update(self):
    self.rect.move_ip( 0, 1 )
    if self.rect.topleft[1] > config["screen_size"][1]:
      self.kill()

  def bulletType(self):
    return self.bType

