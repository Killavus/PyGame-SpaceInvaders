#!/usr/bin/python2.7

import pygame

from Config import *
from Constants import *

class Painter:
  def __init__( self, status, objects ):
    self.status = status
    self.objects = objects
    self.painterSurface = pygame.Surface( config["screen_size"] )
    self.background = pygame.image.load( config["background"] ).convert()

  def paint( self, surface ):
    if self.status.state != constants["state"]["completed"] and self.status.state != constants["state"]["failed"]:
      self.painterSurface.blit( self.background, (0,0) ) 
      self.painterSurface.blit( self.objects.player.getSurface(), self.objects.player.rect )
      self.objects.enemies.draw( self.painterSurface )
      self.objects.powerups.draw( self.painterSurface )
      self.objects.bullets.draw( self.painterSurface )

      if self.objects.player.firingLaser:
        pygame.draw.line( self.painterSurface, (255,0,0), (self.objects.player.rect.centerx, self.objects.player.rect.topleft[1]), (self.objects.player.rect.centerx,0), 1 )
      font = pygame.font.SysFont( 'monospaced', 18 )
      string = "Points: " + str(self.status.points) + " Lives: " + str(self.status.lives) + " AP: " + str(self.objects.player.ap) + " HP: " + str(self.objects.player.hp[1]) + " LP: " + str(self.objects.player.lc)
      if self.status.state == constants["state"]["pause"]:
        string += " [PAUZA]"
      surf = font.render( string, True, (255,255,255) )
      self.painterSurface.blit( surf, (0,0) )
    elif self.status.state == constants["state"]["completed"]:
      self.painterSurface.fill( (0,0,0) )
      font = pygame.font.SysFont( "sans-serif", 60 )
      font2 = pygame.font.SysFont( "sans-serif", 28 )
      winText = font.render( "WINNER!", True, (255,255,255) )
      summary = font2.render( "Punkty: " + str(self.status.points) + " + " + str(self.status.lives * 1000) + " pkt. za zycia!", True, (255,255,255) )
      (wtw,wth) = winText.get_size()
      (sw,sh) = summary.get_size()
      (psw,psh) = self.painterSurface.get_size()

      
      self.painterSurface.blit( winText, (psw/2-wtw/2,psh/2-wth/2) )
      self.painterSurface.blit( summary, (psw/2-sw/2,psh/2-sh/2+wth+10) )
    elif self.status.state == constants["state"]["failed"]:
      self.painterSurface.fill( (0,0,0) )
      font = pygame.font.SysFont( "sans-serif", 60 )
      font2 = pygame.font.SysFont( "sans-serif", 28 )
      winText = font.render( "FAIL!", True, (255,255,255) )
      summary = font2.render( "Punkty: " + str(self.status.points), True, (255,255,255) )
      (wtw,wth) = winText.get_size()
      (sw,sh) = summary.get_size()
      (psw,psh) = self.painterSurface.get_size()

      
      self.painterSurface.blit( winText, (psw/2-wtw/2,psh/2-wth/2) )
      self.painterSurface.blit( summary, (psw/2-sw/2,psh/2-sh/2+wth+10) )
    surface.blit( self.painterSurface, (0,0) )
