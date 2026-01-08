from algoviz.svg import Circle, Rect
import math

class Item:


    def __init__(self, x, y, view, w = 20, h = 20):
        self._x = x
        self._y = y
        self._width = w
        self._height = h
        self._collected = False
        self._rect = Rect(x, y, w, h, view)
        self._rect.set_fill("lightpink")
        self._rect.set_stroke_width(2)

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def get_width(self):
        return self._width

    def get_height(self):
        return self._height

    # Prüft, ob der Spieler das Item einsammelt
    def is_collected(self, player):
        if self._collected:
            return False

        dx = player.get_x() - self._x + self._width/2
        dy = player.get_y() - self._y + self._height/2

        dist = math.sqrt(dx*dx + dy*dy)

        if dist <= self._width + player.get_radius():
            self._collected = True
            self._rect.set_fill("white")  # Item verschwinden lassen
            self._rect.set_stroke_width(0)
