
from pycat.core import Window, Sprite, Scheduler, RotationMode, Label, Color, KeyCode, Player
import random
from random import randint
import random

window = Window(background_image='moon.jpg', enforce_window_limits=False)
window.background_sprite.scale = 2.2

class Jumper(Sprite):
    def on_create(self):
        self.y = 500
        self.x = 1000
        self.scale = 0.45
        self.image = 'jumper.png'
    def on_update(self, dt):
        self.y += 1
        if window.is_key_down(KeyCode.SPACE):
            self.y += -20
        if self.is_touching_any_sprite_with_tag("ufo"):
            self.scale += 0.01

class Ufo(Sprite):
    def on_create(self):
        self.image = "ufo.png"
        self.x =0
        self.y = random.randint(500, 750)
        self.layer = -30
        self.scale = 0.8
        self.add_tag('ufo')
    def on_update(self, dt): 
        self.x += 1
        


 
 
jumper = window.create_sprite(Jumper)



def create_sprite():
    ufo = window.create_sprite(Ufo)
    ufo2 = window.create_sprite(Ufo)
    ufo2.y = ufo.y-500
Scheduler.update(create_sprite, 5)

window.run()


#👍👍👍😭😭😭😄😄😄😂😂😂