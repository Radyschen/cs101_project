from algoviz.svg import Circle
from random import randrange

class Enemy:

    def __init__(self, x, y, radius, raum, lifes = 2, speed = 10):
        self.raum = raum
        self._kreis = Circle(x, y, radius, raum)
        self._kreis.set_fill('orange')
        self.lifes = lifes
        self._speed = speed
        self._d_x = 0
        self._d_y = 0

    #def collission():

    def bewegen(self):
        self._kreis.move_to(self._kreis.get_x() + self._d_y(), self._get_y() + self._d_y)

    def move_to(x,y):
        self.move_to(x,y)

    def lose_life(self):
        return self.lifes = self.get_lifes - 1
        
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

        