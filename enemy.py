from algoviz.svg import Circle
from random import randrange, uniform
import random
import math
from map import Map

class Enemy:

    def __init__(self, x, y, radius, raum, feld, lifes = 2, speed = 5):
        self.raum = raum
        self._kreis = Circle(x, y, radius, raum)
        self._kreis.set_fill('orange')
        self.feld = feld
        self.lifes = lifes
        self.speed = speed
        self._d_x = 0
        self._d_y = 0

    def move(self, px, py):
        if self.checkaggro(px, py):
            self.move_to_player(px, py)
        else:
            self.move_random()

        
    def checkaggro(self, px,py):
        if (abs(px - self.get_x()) < 300) and (abs(py - self.get_y()) < 300):
            return True
        else:
            return False

    def move_to_player(self, px, py):
        dirx, diry = 0, 0
        if abs(px - self.get_x()) < 15:
            if px < self.get_x():
                self.set_dx(-1)
            else:
                self.set_dx(1)
                
        if abs(py - self.get_y()) < 15:
            if py < self.get_y():
                self.set_dy(-1)
            else:
                self.set_dy(1)
                
        self.check_collision()
        
        self._kreis.move_to(self.get_x() + int(self.get_dx() * self.get_speed()), self.get_y() + int(self.get_dy() * self.get_speed()))
    
    
    def check_collision(self):
        next_x = self.get_x() + (self.get_dx()*self.get_speed())
        next_y = self.get_y() + (self.get_dy()*self.get_speed())

        layout = self.feld.get_layout()
        l = 1000
        tile_height = l // len(layout[0])w
        tile_length = l // len(layout)

        next_tile_x = int(next_x / tile_length)
        next_tile_y = int(next_y / tile_height)

        curr_tile_x = int(self.get_x()/ tile_length)
        curr_tile_y = int(self.get_y() / tile_length)

        if layout[next_tile_y][curr_tile_x] == 1:
            self.set_dy(0)

        if layout[curr_tile_y][next_tile_x] == 1:
            self.set_dx(0)

    def update_dir(self):
        x = random.uniform(-0.7, 0.7)
        y = random.uniform(-0.7, 0.7)

        if abs(x) < abs(y):
            if y < 0:
                y = -1
            else:
                y = 1
        else:
            if x < 0:
                x = -1
            else:
                x = 1
                
        dx, dy = x, y

            
    def move_random(self):
        self._kreis.move_to(self.get_x() +(self.get_dx() * self.get_speed()), self.get_y() + (self.get_dy() * self.get_speed()))



        
    
    def move_to(x,y):
        self.move_to(x,y)

    def lose_life(self):
        self.lifes = self.get_lifes() - 1
        
    def get_x(self):
        return self._kreis.get_x()
    def get_y(self):
        return self._kreis.get_y()
    def get_radius(self):
        return self._kreis.get_radius()
    def get_dx(self):
        return self._d_x
    def get_dy(self):
        return self._d_y
    def get_lifes(self):
        return self.lifes
    def get_speed(self):
        return self.speed
    
    def set_x(self, x):
        self._kreis.set_x(x)
    def set_y(self, y):
        self._kreis.set_y(y)
    def set_radius(self, radius):
        self._kreis.set_radius(radius)
    def set_dx(self, d_x):
        self._d_x = d_x
    def set_dy(self, d_y):
        self._d_y = d_y
    def set_lifes(self, lifes):
        self.lifes = lifes
    def set_speed(self, speed):
        self.speed = speed



#class Dummy(Enemy):
    