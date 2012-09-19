#!/usr/bin/python2.7

constants = {
  "state": {
    "pause": 1,
    "ingame": 2,
    "completed": 3,
    "failed": 4
  },
  "version": "1.2.3.4",
  "spritemaps": {
    "battleship": {
      "file": "Resources/spritepacks/battleship.png",
      "dim": (65,70),
      "start": (432,0)
    },
    "battleship_tower": {
      "file": "Resources/spritepacks/battleship.png",
      "dim": (55,40),
      "start": (0,0)
    },
    "insect1": {
      "file": "Resources/spritepacks/enemies.png",
      "dim": (66,40),
      "start": (3,2),
      "delta": (66,0),
      "count": 2
    },
    "insect2": {
      "file": "Resources/spritepacks/enemies.png",
      "dim": (66,45),
      "start": (139,0),
      "delta": (68,0),
      "count": 2
    },
    "insect3": {
      "file": "Resources/spritepacks/enemies.png",
      "dim": (55,40),
      "start": (143,45),
      "delta": (68,0),
      "count": 2
    }
  }
}
