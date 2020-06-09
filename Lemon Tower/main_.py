
# Platformer by Aryan Takalkar.
# Main file

import pygame as pg
import random
from time import sleep
from os import path
from set_ import *
from sprites_ import *

# Initializing the game as a class
class game():
    def __init__(self):
        # Initialize game
        pg.init()
        pg.mixer.init()
        # Get font
        self.font_name = pg.font.match_font(FontName)
        # Opening a pygame window
        self.screen = pg.display.set_mode(size)
        pg.display.set_caption(Title)
        self.running = True
        # Used to manage how fast the screen updates
        self.clock = pg.time.Clock()
        self.load_data()
        
    def load_data(self):
        # Loading the high score
        self.dir = path.dirname(__file__)
        img_dir = path.join(self.dir, "img")
        with open(path.join(self.dir, HS_file), "r+") as f:
            try:
                self.highscore = int(f.read())
            except:
                self.highscore = 0
        # Loading spritesheet
        self.spritesheet = Spritesheet(path.join(img_dir, SPRITESHEET))

    def new(self):
        # Resets game
        self.score = 0
        # Creating sprite groups
        self.all_sprites = pg.sprite.Group()
        self.platforms = pg.sprite.Group()
        # Creating player (the "self" in the bracket is called a refrence, and it gives the Player class information about the game.)
        self.player = Player(self)
        self.all_sprites.add(self.player)
        # Creating platforms
        for p in startingPlatforms:
            plat = Platform(*p)
            self.all_sprites.add(plat)
            self.platforms.add(plat)
        # Run the game
        self.run()

    def run(self):
        # Actual game loop
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):
        # Loop that updates the screen
        self.all_sprites.update()
        # Initializing collisions
        hits = pg.sprite.spritecollide(self.player, self.platforms, False)
        # Checking for collisions when falling (y velocity greater than 0)
        if self.player.vel.y > 0:
            if hits:
                self.player.pos.y = hits[0].rect.top
                self.player.vel.y = 0
        # Scrolling (moving everything down)
        if self.player.vel.y < 0:
            if self.player.pos.y < height/4:
                self.player.pos.y += int(abs(self.player.vel.y))
                for plat in self.platforms:
                    plat.rect.y += (int(abs(self.player.vel.y)))
                    plat.rect.y -= 1
                    # Deleting offscreen platforms
                    if plat.rect.top >= height:
                        plat.kill()
                        # Adding 1 score per deleted platform
                        self.score += 1
        # Spawning new platforms
        while len(self.platforms) < 6:
            w = random.randrange(50, 100)
            x = random.randrange(0, (width - w))
            y = random.randrange(-75, -30)
            p = Platform(x, y, w, 20)
            self.all_sprites.add(p)
            self.platforms.add(p)
        # Game over condition (player falling offscreen)
        if self.player.rect.bottom > height:
            # Scroll down all the way back down to start, cycling through platform list
            for sprite in self.all_sprites:
                sprite.rect.y -= max(int(self.player.vel.y), 10)
                if sprite.rect.bottom < 0:
                    sprite.kill()
        # Reset game after scrolling down through each platform
        if len(self.platforms) == 0:
            self.playing = False

    def events(self):
        # Bit that handles logic & input
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                    self.running = False
            # Jumping when spacebar is pressed
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.player.jump()
                # Exit program if esc key is pressed
                if event.key == pg.K_ESCAPE:
                    self.running = False

    def draw(self):
        # Renders updates on the screen
        self.screen.fill(LIGHTBLUE)
        self.all_sprites.draw(self.screen)
        self.draw_text(str(self.score), 22, WHITE, width/2, 20)
        pg.display.flip()

    def show_start_screen(self):
        # shows start screen
        self.screen.fill(LIGHTBLUE)
        self.draw_text(Title, 50, WHITE, width/2, height/4)
        self.draw_text("Arrow keys to move", 22, WHITE, width/2, height/2)
        self.draw_text("Space to Jump", 22, WHITE, width/2, (height/2 - 50))
        self.draw_text("High Score: " + str(self.highscore), 22, WHITE, width/2, height - 100)
        self.draw_text("Press a button to play", 22, WHITE, width/2, (height*3/4))
        pg.display.flip()
        self.wait_for_keypress()        

    def show_go_screen(self):
        if not self.running:
            return
        # shows game over screen
        self.screen.fill(LIGHTBLUE)
        self.draw_text("Game Over", 50, WHITE, width/2, height/4)
        self.draw_text("Score: " + str(self.score), 22, WHITE, width/2, height/2)
        self.draw_text("Press a button to play again", 22, WHITE, width/2, (height*3/4))
        # Adding high score
        if self.score > self.highscore:
            self.highscore = self.score
            self.draw_text("NEW HIGH!", 24, GREEN, width/2, ((height/2) + 40))
            with open(path.join(self.dir, HS_file), "w") as f:
                f.write(str(self.score))
        else:
            self.draw_text("High Score: " + str(self.highscore), 22, WHITE, width/2, height - 100)
        pg.display.flip()
        self.wait_for_keypress()
    
    def wait_for_keypress(self):
        waitin = True
        while waitin:
            sleep(1/FPS)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    waitin = False
                    self.running = False
                    self.playing = False
                if event.type == pg.KEYUP:
                    waitin = False
    
    def draw_text(self, text, size, colour, x, y):
        font = pg.font.Font(self.font_name, size)
        text_surface = font.render(text, True, colour)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.screen.blit(text_surface, text_rect)


# Creating an objecct "gam" from class game()
gam = game()
gam.show_start_screen()
# Running gam
while gam.running:
    gam.new()
    gam.show_go_screen()

pg.quit()