from algoviz.svg import Circle, Rect
from random import randrange, uniform
import random
import math
from map import Map

class Enemy:

    def __init__(self, x, y, radius, raum, feld, hp = 100, speed = 6):
        self.raum = raum
        self.radius = radius
        self._kreis = Circle(x, y, radius, raum)
        self._start_x = x
        self._start_y = y
        self._kreis.set_fill('orange')
        self.feld = feld
        self.hp = hp
        self.start_hp = hp
        self.speed = speed
        self._d_x = 0
        self._d_y = 0
        self.last_update = 0
        self.aggro = False
        self.last_aggro = 0
        
        self.healthbar_red = Rect(self.get_x() - self.get_radius(), self.get_y() + self.get_radius() + 5, self.get_radius() * 2, self.get_radius() // 2, raum)
        self.healthbar_red.set_fill("red")
                                  
        self.healthbar_green = Rect(self.get_x() - self.get_radius(), self.get_y() + self.get_radius() + 5, self.get_radius() * 2, self.get_radius() // 2, raum)
        self.healthbar_green.set_fill("green")



    
    def move(self, px, py, curr_time):

        if self.checkaggro(px, py, curr_time) or curr_time - self.last_aggro < 2:
            self.move_to_player(px, py)
        else:
            if curr_time - self.last_update >= 2:
                self.update_dir()
                self.last_update = curr_time
            self.move_random()

        self.update_healthbar()


    def update_healthbar(self):
        self.healthbar_red.move_to(self._kreis.get_x() - self.get_radius(), self._kreis.get_y() + self.get_radius() + 5)

        self.healthbar_green.move_to(self._kreis.get_x() - self.get_radius(), self._kreis.get_y() + self.get_radius() + 5)
        
        self.healthbar_green.set_width((self.get_hp() / self.start_hp) * (self.get_radius() * 2))


    def remove_healthbar(self):
        self.healthbar_green.set_fill("white")
        self.healthbar_green.set_stroke_width(0)
        self.healthbar_red.set_fill("white")
        self.healthbar_red.set_stroke_width(0)
        
    def checkaggro(self, px, py, curr_time):
        if (abs(px - self.get_x()) < 150) and (abs(py - self.get_y()) < 150):
            self.aggro = True
            self.last_aggro = curr_time
            return True
        else:
            self.aggro = False
            return False


    
    def move_to_player(self, px, py):

        """
        self.set_dx(0)
        self.set_dy(0)
        
        if abs(px - self.get_x()) > self.radius:
            if px < self.get_x():
                self.set_dx(-1)
            else:
                self.set_dx(1)
                
        if abs(py - self.get_y()) > self.radius:
            if py < self.get_y():
                self.set_dy(-1)
            else:
                self.set_dy(1)
        """
        dx = px - self.get_x()
        dy = py - self.get_y()
    
        dist = math.sqrt(dx * dx + dy * dy)
    
        if dist <= self.radius:
            self.set_dx(0)
            self.set_dy(0)
        else:
            dx /= dist
            dy /= dist
        
            self.set_dx(dx)
            self.set_dy(dy)
                    
            self.check_collision(self.get_dx(), self.get_dy())
            
            self._kreis.move_to(self.get_x() + int(self.get_dx() * self.get_speed()), self.get_y() + int(self.get_dy() * self.get_speed()))

        
    
        
        
        
    
    def check_collision(self, dx, dy):
        speed = self.get_speed()
        x = self.get_x()
        y = self.get_y()
    
        new_x = x + dx * speed
        if self.circle_collides(new_x, y):
            self.set_dx(0)
    
        new_y = y + dy * speed
        if self.circle_collides(x, new_y):
            self.set_dy(0)
    


    def circle_collides(self, x, y):
        r = self.radius
    
        points = [
            # links rechts unten oben
            (x - r, y),
            (x + r, y),
            (x, y - r),
            (x, y + r),

            # 4 zusätzliche randpunkte um kollision robuster zu machen
            (x - r, y - r),
            (x + r, y - r),
            (x - r, y + r),
            (x + r, y + r),
        ]
    
        for px, py in points:
            if self.is_blocked(px, py):
                return True
    
        return False


    def is_blocked(self, x, y):
        layout = self.feld.get_layout()
        rows = len(layout)
        cols = len(layout[0])
    
        tile_w = 1000 / cols
        tile_h = 1000 / rows
    
        tx = int(x // tile_w)
        ty = int(y // tile_h)
    
        if tx < 0 or ty < 0 or tx >= cols or ty >= rows:
            return True
    
        return layout[ty][tx] == 1



    
    # random movement:

    def update_dir(self):#
        """
        x = random.uniform(-0.5, 0.5)
        y = random.uniform(-0.5, 0.5)

        
        if abs(x) < abs(y):
            if y < 0:
                y = -0.7
            else:
                y = 0.7
        else:
            if x < 0:
                x = -0.7
            else:
                x = 0.7
        """

        dir = [(0.5,0), (-0.5,0), (0,0.5), (0,-0.5), (0.75,0), (-0.75,0),(0,0.75),(0,-0.75),(0,0)]

        x, y = random.choice(dir)
                
        self.set_dx(x)
        self.set_dy(y)

            
    def move_random(self):
        self.check_collision(self.get_dx(), self.get_dy())
        
        self._kreis.move_to(self.get_x() + self.get_dx() * self.get_speed(), self.get_y() + self.get_dy() * self.get_speed())




    def hits_player(self, px, py):
        dx = px - self.get_x()
        dy = py - self.get_y()
    
        dist = math.sqrt(dx*dx + dy*dy)

        if dist <= self.get_radius() * 2:
            return True
            
        return  False
    
    def move_to(x,y):
        self._kreis.move_to(x,y)

    def lose_life(self, n):
        self.hp = self.get_hp() - n
        

    
        
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
    def get_hp(self):
        return self.hp
    def get_speed(self):
        return self.speed
    def get_start_x(self):
        return self._start_x
    def get_start_y(self):
        return self._start_y
    
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
    def set_hp(self, lifes):
        self.hp = lifes
    def set_speed(self, speed):
        self.speed = speed



class Dummy(Enemy):
    def __init__(self, x, y, radius, raum, feld, hp = 100, speed = 6):
        super().__init__(x, y, radius, raum, feld, hp, speed)
        self._start_x = 500
        self._start_y = 500

    def move(self, px, py, curr_time):
        self.update_healthbar()
    
    def hits_player(self, px, py):
        pass
    
    