from algoviz.svg import Circle, Rect, Image
import math

class Item:


    def __init__(self, x, y, view, type, image, w = 20, h = 20,):
        self._x = x
        self._y = y
        self._width = w
        self._height = h
        self._type = type
        self._collected = False
        self.image = Image(image, x, y, w, h, view)
        #self._rect = Rect(x, y, w, h, view)
        #self._rect.set_fill("lightpink")
        #self._rect.set_stroke_width(2)

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def get_width(self):
        return self._width

    def get_height(self):
        return self._height

    def get_type(self):
        return self._type

    # Prüft, ob der Spieler das Item einsammelt
    def is_collected(self, player, x, y, w, h, view):
        if self._collected:
            return False

        dx = player.get_x() - self._x + self._width/2
        dy = player.get_y() - self._y + self._height/2

        dist = math.sqrt(dx*dx + dy*dy)

        if dist <= self._width + player.get_radius():
            self._collected = True
            fill = Rect( x, y, w, h, view)
            fill.set_fill("white")  # Item verschwinden lassen
            fill.set_stroke_width(0)
            return True
        return False
