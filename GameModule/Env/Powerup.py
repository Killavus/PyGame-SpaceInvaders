#!/usr/bin/python2.7

import pygame
from GameModule.Config import *

class Powerup(pygame.sprite.Sprite):
  def __init__(self):
    super(Powerup,self).__init__()

  
  def move(self):
    self.rect.move_ip( 0, self.speed )

  def update(self):
    self.move()
    if self.rect.topleft[1] > config["screen_size"][1]:
      self.kill()
