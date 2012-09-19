#!/usr/bin/python2.7

import pygame

class SpriteUnpacker:
  def __init__(self, spriteFile):
    self.sequences = {}
    self.spriteMap = pygame.image.load(spriteFile).convert()

  def createSequence( self, name, dim, startPos, nextVec, count ):
    self.sequences[name] = Sequence( self.spriteMap, dim, startPos, nextVec, count )
  
class Sequence:
  def __init__( self, spriteMap, dim, startPos, nextVec, count ):
    self.images = []
    (sx,sy) = startPos
    (nx,ny) = nextVec
    ptr = (ptrx,ptry) = startPos
    i = 0
    while i < count:
      self.images.append( spriteMap.subsurface( pygame.Rect( ptr, dim ) ) )
      ptr = (ptrx + nx,ptry + ny)
      i += 1

