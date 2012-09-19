#!/usr/bin/python2.7

import pygame
from Powerup import Powerup

class UpgradePowerup(Powerup):
  def __init__(self, x, y, battleship):
    super(UpgradePowerup,self).__init__()

    self.battleship = battleship

    font = pygame.font.SysFont( "serif", 18 )
    render = font.render( "UPG", True, (245,184,0) )

    self.image = render
    self.rect = self.image.get_rect()
    self.rect.centerx = x
    self.rect.centery = y
    
    self.speed = 3

  def makeEffects(self):
    self.battleship.upgraded = True
    self.kill()
  
