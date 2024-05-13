543# This file was created by: Sebastian

import pygame as pg
from setting import *
from math import *

vec = pg.math.Vector2
#Vector code for Mob, to follow player coordinates
def collide_with_walls(sprite, group, dir):
    if dir == "x":
        hits = pg.sprite.spritecollide(sprite, group, False)
        if hits:
            if hits[0].rect.centerx > sprite.rect.centerx:
                sprite.pos.x = hits[0].rect.left - sprite.rect.width / 2
            if hits[0].rect.centerx < sprite.rect.centerx:
                sprite.pos.x = hits[0].rect.right + sprite.rect.width / 2
            sprite.vel.x = 0
            sprite.rect.centerx = sprite.pos.x
    if dir == "y":
        hits = pg.sprite.spritecollide(sprite, group, False)
        if hits:
            if hits[0].rect.centery > sprite.rect.centery:
                sprite.pos.y = hits[0].rect.top - sprite.rect.height / 2
            if hits[0].rect.centery < sprite.rect.centery:
                sprite.pos.y = hits[0].rect.bottom + sprite.rect.height / 2
            sprite.vel.y = 0
            sprite.rect.centery = sprite.pos.y
#Copied from AI, - Magically Worked 
 
# write a player class
class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        #self.image = pg.Surface((TILESIZE, TILESIZE))
        #self.image.fill(GREEN)
        self.image = game.player_img
        self.rect = self.image.get_rect()
        self.vx, self.vy = 0, 0
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.moneybag = 0
        self.speed = 300
        self.start = (self.x, self.y)
        self.colorchange = False
        #coins collect
    def death(self) :
        self.x, self.y = self.start
    def get_keys(self):
        self.vx, self.vy = 0, 0
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT] or keys[pg.K_a]:
            self.vx = -self.speed 
            self.vx = -PLAYER_SPEED
        if keys[pg.K_RIGHT] or keys[pg.K_d]:
            self.vx = -self.speed 
            self.vx = PLAYER_SPEED
        if keys[pg.K_UP] or keys[pg.K_w]:
            self.vy = -self.speed 
            self.vy = -PLAYER_SPEED
        if keys[pg.K_DOWN] or keys[pg.K_s]:
            self.vy = -self.speed 
            self.vy = PLAYER_SPEED
            #keybinds and speed for player
            #speed change for speed boost
            
    def collide_with_walls(self, dir):
        if dir == 'x':
            hits = pg.sprite.spritecollide(self, self.game.walls, False )
            if hits:
                if self.vx > 0:
                    self.x = hits[0].rect.left - self.rect.width
                if self.vx < 0:
                    self.x = hits[0].rect.right
                self.vx = 0
                self.rect.x = self.x
                #collision for walls/deathblock
        if dir == 'y':
            hits = pg.sprite.spritecollide(self, self.game.walls, False )
            if hits:
                if self.vy > 0:
                    self.y = hits[0].rect.top - self.rect.height
                if self.vy < 0:
                    self.y = hits[0].rect.bottom
                self.vy = 0
                self.rect.y = self.y
    def collide_with_deathblocks(self, dir):
        if dir == 'x':
            hits = pg.sprite.spritecollide(self, self.game.deathblocks, False )
            if hits:
                self.death()
    def collide_with_Speedboost(self, dir) :
        #COLLISION FOR SPEED BOOST
        if dir == "x":
            hits = pg.sprite.spritecollide(self,self.game.Speedboost, True)
                
    def collide_with_group(self, group, kill):
            hits = pg.sprite.spritecollide(self, group, False)
            if hits:
                if str(hits[0].__class__.__name__) == "Colorchange":
                    self.colorchange = True
        
    def collide_with_mob(self, dir):
        if dir == 'x':
            hits = pg.sprite.spritecollide(self,self.game.mob, False)
                
                        
#INCREASING SPEED, WHEN COLLIDING WITH SPEED BOOST
        
        
    # old motion
    # def move(self, dx=0, dy=0):
    #     self.x += dx
    #     self.y += dy

    # UPDATE THE UPDATE
    def update(self):
        # self.rect.x = self.x
        # self.rect.y = self.y
        self.get_keys()
        self.x += self.vx * self.game.dt
        self.y += self.vy * self.game.dt
        self.rect.x = self.x
        self.collide_with_walls('x')
        self.collide_with_deathblocks('x')
        self.rect.y = self.y
        self.collide_with_walls('y')
        self.collide_with_deathblocks('x')
        self.collide_with_group(self.game.mobs, False)
        self.collide_with_group(self.game.colorchangers, True)
        # self.rect.x = self.x * TILESIZE
        # self.rect.y = self.y * TILESIZE
        if self.colorchange:
            self.image = self.game.Supermario_img
        # If image colides with group, image changes to :

class Mob(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.mobs
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        #self.image = pg.Surface((TILESIZE, TILESIZE))
        #self.image.fill(ORANGE)
        self.image = self.game.mobs_img
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        # self.vx, self.vy = 100, 100
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.speed = 100
        self.pos = vec(x, y) * TILESIZE
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.rect.center = self.pos
        self.rot = 0
        self.speed = 150

    def update(self):
        #if abs(self.game.p1.rect.x - self.x)*32 < 5:
        #    if abs(self.game.p1.rect.y - self.y)*32 < 5:
        self.rot = (self.game.p1.rect.center - self.pos).angle_to(vec(1, 0))
        self.rect.center = self.pos
        self.acc = vec(self.speed, 0).rotate(-self.rot)
        self.acc += self.vel * -1
        self.vel += self.acc * self.game.dt
        self.pos += self.vel * self.game.dt + 0.5 * self.acc * self.game.dt ** 2
        collide_with_walls(self, self.game.walls, 'x')
        collide_with_walls(self, self.game.walls, 'y')
        collide_with_walls(self, self.game.fakewalls, 'x')
        collide_with_walls(self, self.game.fakewalls, 'y')
        #Updates added to collide with Fake wall


class Wall(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.walls
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(LIGHTGREY)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
        self.speed = 0
        # ADDS WALLS TO THE GAME( OUTER)
    def update(self):
        # self.rect.x += 1
        self.rect.x += TILESIZE * self.speed
        # self.rect.y += TILESIZE * self.speed
        if self.rect.x > WIDTH or self.rect.x < 0:
            self.speed *= -1
        # if self.rect.y > HEIGHT or self.rect.y < 0:
        #     self.speed *= -1

class FakeWall(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.fakewalls
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(LIGHTGREY)
        self.rect = self.image.get_rect()
        self.image = game.fakewalls_img
        #Fake Wall to hide from enemies
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
class Deathblock(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.deathblocks
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(RED)
        self.image = game.deathblocks_img
        self.rect = self.image.get_rect()
        # kills player and respawns it where it spawned before
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
    

class Speedboost(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.Speedboost 
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(RED)
        self.image = game.Speedboost_img
        # doubles the speed of player when interacting
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

class Colorchange(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.colorchangers
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.image = game.colorchangers_img
        self.x = x
        self.y = y
        #Customizes Player image
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
        
