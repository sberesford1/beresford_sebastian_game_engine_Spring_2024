543# This file was created by: Sebastian

import pygame as pg
from setting import *
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
        #coins collect
    def death(self) :
        self.x = self.game.p1col *TILESIZE
        self.y = self.game.p1row *TILESIZE
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
            #self.vy = PLAYER_SPEED
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
            if str(hits[0].__class__.__name__) == "Coin":
                self.moneybag += 1
            if str(hits[0].__class__.__name__) == "Speedboost":
                #self.vx = PLAYER_SPEED = 800
                 self.speed += 300
                 if str(hits[0].__class__.__name__) == "Mob":
                    self.detath()
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
        # self.rect.x = self.x * TILESIZE
        # self.rect.y = self.y * TILESIZE
        # UPDATES GAME TO KEEP UP

class Mob(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.mobs
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(ORANGE)
        #self.image = self.game.mob_img
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        # self.vx, self.vy = 100, 100
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.speed = 100


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
        #self.image = game.deathblocks_img
        # doubles the speed of player when interacting
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

class Coin(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.coins
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
        # ADDS A COIN, THAT U CAN COLLECT
