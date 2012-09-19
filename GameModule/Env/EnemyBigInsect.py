#!/usr/bin/python2.7

import pygame
import math
import random

from Enemy                     import Enemy
from BigInsectBullet           import BigInsectBullet
from GameModule.SpriteUnpacker import *
from GameModule.Config         import *
from GameModule.Constants      import *

class EnemyBigInsect(Enemy):
  def __init__(self, x, y, bulletsGroup):
    super( EnemyBigInsect, self ).__init__(550)

    self.spawnTime = 60
    self.spawnFrames = self.spawnTime
    self.destroyTime = 30
    self.destroyFrames = self.destroyTime
    self.bullets = bulletsGroup
    self.bulletChance = 3
    self.chance = 0
    self.destroyed = False
    self.spawned = False

    insectConst = constants["spritemaps"]["insect2"]
    self.insectConst = insectConst

    unpacker = SpriteUnpacker( insectConst["file"] )
    unpacker.createSequence( "insect", insectConst["dim"], insectConst["start"], insectConst["delta"], insectConst["count"] )

    self.images = unpacker.sequences["insect"].images
    
    self.rect = self.images[0].get_rect()
    self.rect.centerx = x
    self.rect.centery = y

    self.image = unpacker.sequences["insect"].images[0]
  
    self.frameTick = 0
    self.actualFrame = 0

  def update(self):
    if self.rect.topright[0] >= config["screen_size"][0] or self.rect.topleft[0] <= 0:
      self.setDirection()
    self.move(1)

    self.image = self.images[self.actualFrame]
    self.image.set_colorkey( self.image.get_at( (0,0) ) )
    self.drawHP()
    self.frameTick += 1

    if self.frameTick == config["framerate"]/2:
      self.actualFrame += 1
      self.actualFrame %= self.insectConst["count"]
      self.frameTick = 0

    if self.spawnFrames > 0:
      self.spawnFrames -= 1
      self.image.set_alpha( 255 - math.floor((float(self.spawnFrames) / self.spawnTime) * 255) )
    else:
      self.spawned = True
      self.image.set_alpha( 255 )

    if self.destroyed == True:
      if self.destroyFrames > 0:
        self.destroyFrames -= 1
        self.image.set_alpha( math.floor( (float(self.destroyFrames) / self.destroyTime) * 255 ) )
      else:
        self.kill()


    self.chance = random.randint(0,1000)

    if self.spawned == True and self.destroyed == False and self.chance <= self.bulletChance:
      self.spawnBullet().add(self.bullets)      
        
  def spawnBullet(self):
    return BigInsectBullet( self.rect.centerx, self.rect.topleft[1] + 20 )
  
