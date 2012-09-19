#!/usr/bin/python2.7

import pygame
import math

from ShipBullet                import ShipBullet
from BattleObject              import BattleObject
from GameModule.Config         import *
from GameModule.Constants      import *
from GameModule.SpriteUnpacker import *

class BattleShip(BattleObject):
  def __init__(self, status):
    super(BattleShip, self).__init__( config["battleship"]["hp"] )
    
    self.status = status
    self.ap = config["battleship"]["ap"]
    self.lc = config["battleship"]["lc"]
    self.fireCooldown = 0
    self.firingLaser = False
    self.upgraded = False
    self.destroyed = False
    self.destroyTime = config["framerate"]/2
    self.destroyFrames = self.destroyTime
    self.shield = False
    self.shieldTicks = 0
    self.shieldMax = math.ceil(config["framerate"]/4)
    towerData = constants["spritemaps"]["battleship_tower"]
    shipData = constants["spritemaps"]["battleship"]


    unpacker = SpriteUnpacker( constants["spritemaps"]["battleship"]["file"] )

    unpacker.createSequence( "battleship", shipData["dim"], shipData["start"], (0,0), 1 )
    unpacker.createSequence( "battleship_tower", towerData["dim"], towerData["start"], (0,0), 1 )

    self.image = unpacker.sequences["battleship"].images[0]
    self.image.set_colorkey( self.image.get_at( (0,0) ) )
    self.tower = unpacker.sequences["battleship_tower"].images[0]
    self.tower.set_colorkey( self.image.get_at( (0,0) ) )
    self.rect = self.image.get_rect()
    self.rect.centerx = config["screen_size"][0]/2
    self.rect.centery = config["screen_size"][1] - constants["spritemaps"]["battleship"]["dim"][1]

  def toggleUpgraded(self):
    self.upgraded = not self.upgraded

  def getSurface(self):
    (w,h) = self.image.get_size()
    (tw,th) = self.tower.get_size()
    surf = pygame.Surface( (w,h) )
    surf.blit( self.image, (0,0) )
    surf.set_colorkey( surf.get_at( (0,0) ) )
    if self.upgraded == True:
      surf.blit( self.tower, (w/2-tw/2,h/2-th/2) )
    if self.shield == True:
      pygame.draw.circle( surf, pygame.Color( 0,0,255,50 ), (w/2,h/2), min(w,h)/2, 2 )
    return surf

  def fire( self, bulletType ):
    if bulletType == "bullet":
      self.fireCooldown = config["framerate"]/2
      y = self.rect.centery - self.image.get_size()[1]/2 - 20
      if self.upgraded == True:
        return ( 3,
            ( ShipBullet( self.rect.centerx, y ),
              ShipBullet( self.rect.centerx+30, y ),
              ShipBullet( self.rect.centerx-30, y )
            )
        )
      else:
        return ( 1, ShipBullet( self.rect.centerx, y ) )
    elif bulletType == "laser" and self.lc > 0:
      self.firingLaser = True

  def stopFire( self, bulletType ):
    if bulletType == "bullet":
      pass
    elif bulletType == "laser":
      self.firingLaser = False

  def move( self, x ):
    self.rect.centerx = max( self.image.get_size()[0]/2, self.rect.centerx + x )
    self.rect.centerx = min( config["screen_size"][0] - self.image.get_size()[0]/2, self.rect.centerx )

  def toggleShield( self ):
    self.shield = not self.shield

  def update( self ):
    if self.fireCooldown > 0:
      self.fireCooldown -= 1
    if self.shield == True:
      self.shieldTicks += 1
      if self.shieldTicks == self.shieldMax:
        self.shieldTicks = 0
        self.ap -= 1 
    if self.ap <= 0:
      self.shield = False
      self.shieldTicks = 0

    if self.destroyed == True:
      if self.destroyFrames > 0:
        self.destroyFrames -= 1
        self.image.set_alpha( math.floor( (float(self.destroyFrames) / self.destroyTime) * 255 ) )

  def makeHit( self, hp ):
    super( BattleShip, self ).makeHit(hp)
    if self.destroyed == True:
      self.status.lives -= 1
