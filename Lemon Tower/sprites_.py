
# Platformer by Aryan Takalkar
# Sprites file

import pygame as pg
from set_ import *

vec = pg.math.Vector2

# Creating a spritesheet class
class Spritesheet():
    # Loading and parsing the spritesheet
    def __init__(self, filename):
        self.spritesheet = pg.image.load(filename).convert()
        
    def get_image(self, x, y, w, h):
        # Cropping sprite out of the spritesheet
        image = pg.Surface((w, h))
        image.blit(self.spritesheet, (0, 0), (x, y, w, h))
        image = pg.transform.scale(image, (w//2, h//2))
        return image

#
# Creating a class Player
class Player(pg.sprite.Sprite):
    def __init__(self, game):
        # Giving the Player class access to game data
        self.game = game
        # Initializing the player
        pg.sprite.Sprite.__init__(self)
        # Tracking animations
        self.walking = False
        self.jumping = False
        self.current_frame = 0
        # Setting the size, colour, and staring position of the player
        self.image = self.game.spritesheet.get_image(614, 1063, 120, 191)
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (width/2, height/2)
        self.pos = vec(width/2, height/2)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        
    def jump(self):
        # Jumping
        # Checking if the player is standing on something. 
        # The game does this by shifting the player down one pixel, checking collisions, and then moving the player back up without updating the screen.
        self.rect.x += 1
        hits = pg.sprite.spritecollide(self, self.game.platforms, False)
        self.rect.x -= 1
        if hits:
            self.vel.y = -playerJumpHeight
    
    def update(self):
        # Updating player sprite position
        self.acc = vec(0, playerGravity)
        keys = pg.key.get_pressed()
        # Moving left
        if keys[pg.K_LEFT]:
            self.acc.x = 0 - playerAcceleration
        # Moving right
        if keys[pg.K_RIGHT]:
            self.acc.x = playerAcceleration
        
        # Applying acceleration and velocity
        self.acc.x += self.vel.x * playerFriction
        self.vel += self.acc
        self.pos += self.vel + (0.5 * self.acc)
        
        # Wrapping around the screen
        if self.pos.x > width:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = width
        
        # Applying changes in position (player position
        self.rect.midbottom = self.pos

#
# Creating a class Platform
class Platform(pg.sprite.Sprite):
    # Platorms take 4 arguments: x position, y position, width, and height.
    def __init__(self, x, y, w, h):
        pg.sprite.Sprite.__init__(self)
        # Setting the size, colour, and staring position of the platform
        self.image = pg.Surface((w, h))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

#