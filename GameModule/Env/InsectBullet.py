#!/usr/bin/python2.7

import pygame

from GameModule.Config import *
from Bullet import Bullet

class InsectBullet(Bullet):
  def __init__(self, x, y):
    super( InsectBullet, self ).__init__()
    self.image = pygame.Surface( (5,20) )
    self.image.fill( (255,204,61) )
    
    self.rect = self.image.get_rect()
    self.rect.centerx = x
    self.rect.centery = y

    self.bType = "enemy"

    self.hit = 20

  def update(self):
    self.rect.move_ip( 0, 3 )
    if self.rect.topleft[1] > config["screen_size"][1]:
      self.kill()

  def bulletType(self):
    return self.bType

