#!/usr/bin/python2.7
# Encoding: utf-8

from sys                   import exit

import random
import pygame
from pygame.locals         import *

from GameModule.Constants  import *
from GameModule.Config     import *

from GameModule.Objects    import *
from GameModule.Mapper     import *
from GameModule.Status     import *
from GameModule.Painter    import *

import GameModule.Env

class Game:
  def __init__(self):
    pygame.init()
    pygame.display.set_caption( "Space Invaders v" + constants["version"] )
    self.screen = pygame.display.set_mode( config["screen_size"] )
    self.clock = pygame.time.Clock()
    self.nextFall = -1

    # Status, klasa odpowiadająca za przechowywanie informacji o punktach, życiach i aktualnym stanie naszego statku.
    self.status = Status()
    
    # Objects, klasa przechowująca obiekty będące aktualnie w grze - pociski, przeciwników, gracza itp. 
    self.objects = Objects(self.status)
    
    # Mapper, klasa przechowująca informacje o mapie i wczytująca mapy z pliku:
    self.mapper = Mapper( self.objects )
    self.mapper.load( "Resources/map.data" )

    # Painter, klasa odpowiadająca za rysowanie na ekranie.
    self.painter = Painter( self.status, self.objects )

  def eventLoop(self):
    for event in pygame.event.get():
      if self.status.state == constants["state"]["ingame"]:
        if event.type == KEYDOWN:
          if event.key == K_LSHIFT:
            self.objects.player.toggleShield()
        
        if event.type == KEYUP:
          if event.key == K_LSHIFT and self.objects.player.shield == True:
            self.objects.player.toggleShield()
          if event.key == K_LCTRL:
            self.objects.player.stopFire( "laser" )

      if event.type == KEYDOWN:
        if event.key == K_p and self.status.state == constants["state"]["ingame"]:
          self.status.state = constants["state"]["pause"]
        elif event.key == K_p and self.status.state == constants["state"]["pause"]:
          self.status.state = constants["state"]["ingame"]

      if event.type == QUIT:
        exit(0)

  def keyboardLoop(self):
    key = pygame.key.get_pressed()
    if self.status.state == constants["state"]["ingame"]:
      if key[K_LEFT]:
        self.objects.movePlayer( K_LEFT )
      elif key[K_RIGHT]:
        self.objects.movePlayer( K_RIGHT )
      if key[K_SPACE]:
        if self.objects.player.fireCooldown == 0:
          bullets = self.objects.player.fire( "bullet" )
          if bullets[0] < 2:
            bullets[1].add( self.objects.bullets )
          else:
            for i in xrange(bullets[0]):
              bullets[1][i].add( self.objects.bullets )
      elif key[K_LCTRL]:
        if self.objects.player.lc > 0:
          self.objects.player.fire( "laser" )
          self.objects.player.lc -= 1

  def updateLoop(self):
    if self.status.state == constants["state"]["ingame"]:
      self.objects.updateBullets()
      self.objects.updateEnemies()
      self.objects.updatePowerups()
      self.objects.player.update()
      collisionsEnemiesWithin = pygame.sprite.groupcollide( self.objects.enemies, self.objects.enemies, False, False )
      collisionsEnemies = pygame.sprite.groupcollide( self.objects.enemies, self.objects.bullets, False, False )
      collisionsPlayer = pygame.sprite.spritecollide( self.objects.player, self.objects.bullets, False )
      collisionsPlayerPowerups = pygame.sprite.spritecollide( self.objects.player, self.objects.powerups, False )

      turnToLeft = False
      turnToRight = False

      for enemy in iter(self.objects.enemies):
        if enemy.destroyed == True or enemy.spawnFrames > 0:
          continue

        if self.objects.player.firingLaser == True:
          (cx,cy) = self.objects.player.rect.center
         
          if enemy.rect.topleft[0] < cx and enemy.rect.topright[0] > cx:
            enemy.makeHit(1)
            if enemy.destroyed == True:
              self.generatePowerup( enemy.rect.centerx, enemy.rect.centery )
              self.status.points += 100


      for enemy,bullets in collisionsEnemies.iteritems():
        if enemy.destroyed == True:
          continue
        if enemy.spawnFrames > 0:
          continue

        for bullet in bullets:
          if enemy.destroyed:
            continue

          if bullet.bulletType() == "player":
            enemy.makeHit(bullet.hit)
            if enemy.destroyed == True:
              self.generatePowerup( enemy.rect.centerx, enemy.rect.centery )
              self.status.points += 100
            bullet.kill()

      for bullet in collisionsPlayer:
        if bullet.bulletType() == "enemy":
          if self.objects.player.shield == True:
            self.objects.player.ap -= bullet.hit
            if self.objects.player.ap < 0:
              self.objects.player.makeHit(-self.objects.player.ap)
              self.objects.player.ap = 0
          else:
            self.objects.player.makeHit(bullet.hit)
          bullet.kill()

      for powerup in collisionsPlayerPowerups:
        powerup.makeEffects()
      
      if self.objects.player.destroyed == True and self.objects.player.destroyFrames == 0:
        self.objects.player = BattleShip(self.status)

      if self.nextFall > 0:
        self.nextFall -= 1
      elif self.nextFall == 0:
        self.nextFall -= 1
        ret = self.mapper.nextStage()
        if ret == False:
          self.status.state = constants["state"]["completed"]

      if len(self.objects.enemies) == 0 and self.nextFall == -1:
        self.nextFall = config["framerate"]*5

      if self.status.lives == 0:
        self.status.state = constants["state"]["failed"]


  def generatePowerup(self, x, y):
    roll = random.randint(0,100)
    if roll < config["powerup_chance"]:
      roll2 = random.randint(0,3)
      obj = None
      if roll2 == 0:
        obj = APPowerup( x, y, self.objects.player )
      elif roll2 == 1:
        obj = UpgradePowerup( x, y, self.objects.player )
      elif roll2 == 2:
        obj = HPPowerup( x, y, self.objects.player )
      elif roll2 == 3:
        obj = LCPowerup( x, y, self.objects.player )
      obj.add( self.objects.powerups )

  def start(self):
    while True:
      self.clock.tick( config["framerate"] )

      self.eventLoop()
      self.keyboardLoop()
      self.updateLoop()
      
      self.painter.paint( self.screen )
      pygame.display.update()

# Tworzymy obiekt gry i zaczynamy ją.
game = Game()
game.start()
