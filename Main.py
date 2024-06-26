    # This file was created by: Sebastian

# goals,rules, feedback, freedom, verb (action a player makes)
import pygame as pg
from setting import *
from Sprites import *
import sys
from random import randint
from os import path

# create a game class 
class Game:
    # behold the methds...
    def __init__(self):
        pg.init()
        # 
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        # 
        pg.display.set_caption("My First Video Game")
        # 
        self.clock = pg.time.Clock()    
        pg.key.set_repeat(500, 100)
        self.running = True
        # later on we'll story game info with this
        self.load_data()
    def load_data(self):
        game_folder = path.dirname(__file__)
        img_folder = path.join(game_folder,'images')
        self.player_img = pg.image.load(path.join(img_folder, 'Bettermario.png')).convert_alpha()
        self.deathblocks_img = pg.image.load(path.join(img_folder, 'betterspikes.png')).convert_alpha()
        self.mobs_img = pg.image.load(path.join(img_folder, 'Goomba.png')).convert_alpha()
        self.fakewalls_img = pg.image.load(path.join(img_folder, 'Fakewall.png')).convert_alpha()
        self.Supermario_img = pg.image.load(path.join(img_folder, 'Supermario.png')).convert_alpha()
        self.colorchangers_img = pg.image.load(path.join(img_folder, 'Colorchange.png')).convert_alpha()
        self.snd_folder = path.join(game_folder, 'sounds')
        self.map_data = []
        '''
        The with statement is a context manager in Python. 
        It is used to ensure that a resource is properly closed or released 
        after it is used. This can help to prevent errors and leaks.



        Want to make the game challenging by adding
         Weapons and mobs - make the game have a main goal or ending.   

        '''
        with open(path.join(game_folder, 'map.txt'), 'rt') as f:
            for line in f:
                print(line)
                self.map_data.append(line)
                print(self.map_data)
    def new(self):
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.deathblocks = pg.sprite.Group()
        self.mobs = pg.sprite.Group()
        self.Speedboost = pg.sprite.Group()
        self.fakewalls = pg.sprite.Group()
        self.colorchangers = pg.sprite.Group()
        #pg.mixer.music.load(path.join(self.snd_folder))
        # self.player = Player(self, 10, 10)
        # self.all_sprites.add(self.player)
        # for x in range(10, 20):x``
        #     Wall(self, x, 5)
        for row, tiles in enumerate(self.map_data):
            print(row)
            for col, tile in enumerate(tiles):
                print(col)
                if tile == '1':
                    print("a wall at", row, col)
                    Wall(self, col, row)
                if tile == 'C':
                    self.p1col = col
                    self.p1row = row
                    self.p1 = Player(self, self.p1col, self.p1row)
                    self.player = Player(self, col, row)
                if tile == 'd':
                    Deathblock(self,col,row)
                if tile == 'M':
                    Mob(self, col, row)
                if tile == 'F':
                    FakeWall(self,col,row)
                if tile == 'c':
                    Colorchange(self,col,row)
                if tile == 'S':   
                    Speedboost(self, col, row)
                    
                        #letters can determine where each item/player spawns on map
    def run(self):
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            # this is input
            self.events()
            # this is processing
            self.update()
            # this output
            self.draw()
            #frames per second

    def quit(self):
        pg.quit()
        sys.exit()
    # methods
    def input(self): 
        pass
    def update(self):
        self.all_sprites.update()
        #updates the game to keep up
    
    def draw_grid(self):
        for x in range(0, WIDTH, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))
            #grid size and coords

    def draw(self):
        self.screen.fill(BGCOLOR)
        self.draw_grid()
        self.all_sprites.draw(self.screen)
        pg.display.flip()

    def events(self):
            # listening for events
            for event in pg.event.get():
                # when you hit the red x the window closes the game ends
                if event.type == pg.QUIT:
                    self.quit()
                    print("the game has ended..")
                # keyboard events
                # if event.type == pg.KEYDOWN:
                #     if event.key == pg.K_LEFT:
                #         self.player.move(dx=-1)
                # if event.type == pg.KEYDOWN:
                #     if event.key == pg.K_RIGHT:
                #         self.player.move(dx=1)
                # if event.type == pg.KEYDOWN:
                #     if event.key == pg.K_UP:
                #         self.player.move(dy=-1)
                # if event.type == pg.KEYDOWN:
                #     if event.key == pg.K_DOWN:
                #         self.player.move(dy=1)
    def show_start_screen(self):
        pass
    def show_go_screen(self):
        pass
    def show_start_screen(self):
        self.screen.fill(BGCOLOR)
        self.draw_text(self.screen, "This is the start screen", 24, WHITE, WIDTH/2 - 32, 2)
        pg.display.flip()
        self.wait_for_key(e)
        #start screen, beginning the game

    def wait_for_key(self):
        waiting = True
        while waiting:
            self.clock.tick(FPS)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    waiting = False
                    self.quit()
                if event.type == pg.KEYUP:
                    waiting = False
    #def run(self):
        #pg.mixer.music.play(loops=-1)
####################### Instantiate game... ###################
g = Game()
# g.show_go_screen()
#g.show_start_screen()
while True:
   # g.show_go_screen()
    g.new()
    g.run()