from algoviz.svg import Circle
from random import randrange

class Player:

    def __init__(self, x, y, radius, raum):
        self._raum = raum
        self._kreis = Circle(x, y, radius, raum)
        self._kreis.set_fill("lightblue")
        #self._status = status
        #self._gesundungs_zeit = gesundungs_zeit
        self._speed = 10
        self._d_x = 0
        self._d_y = 0


    def bewegen(self):
        """Bewegt die Person in x- und y-Richtung entsprechend der eigenen d_x und d_y"""
        self._kreis.move_to(self._kreis.get_x() + self._d_x, self._kreis.get_y() + self._d_y)

    def move_to(x,y):
        self._kreis.move_to(x,y)
       

    def get_x(self):
        return self._kreis.get_x()
    def get_y(self):
        return self._kreis.get_y()
    def get_radius(self):
        return self._kreis.get_radius()
    def get_status(self):
        return self._status
    def get_gesundungs_zeit(self):
        return self._gesundungs_zeit
    def get_dx(self):
        return self._d_x
    def get_dy(self):
        return self._d_y
    def get_speed(self):
        return self._speed
    
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
    def set_speed(self, speed):
        self._speed = speed
