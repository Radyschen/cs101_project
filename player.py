from algoviz.svg import Circle, SVGView
from random import randrange
import math

class Player:

    def __init__(self, x, y, radius, raum):
        self._raum = raum
        self._kreis = Circle(x, y, radius, raum)
        self._kreis.set_fill("lightblue")
        self._speed = 10
        self._d_x = 0
        self._d_y = 0
        self._hp = 100 # Leben/health points
        self._attack_radius_ratio = 4
        self._last_attack_time = 0
        self._last_hit = 0
        self._cooldown = 0.5
        self._hit_cooldown = 2
        self.attack_circle = Circle(x,y, self.get_radius() * self._attack_radius_ratio, self._raum)
        self.attack_circle.set_fill("white")

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
    def get_hp(self):
        return self._hp
    def get_last_attack_time(self):
        return self._last_attack_time
    
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
    def set_hp(self, hp):
        self._hp = hp
    def set_last_attack_time(self, time):
        self._last_attack_time = time
    def lose_hp(self, n):
        self._hp = self.get_hp() - n

    def to_front(self):
        self._kreis.to_front()

    def bewegen(self):
        self.attack_circle.set_fill_rgb(0,0,0,0)
        self.attack_circle.set_stroke_width(0)
        self.attack_circle.move_to(self.get_x(), self.get_y())
        
        """Bewegt die Person in x- und y-Richtung entsprechend der eigenen d_x und d_y"""
        self._kreis.move_to(self._kreis.get_x() + self._d_x, self._kreis.get_y() + self._d_y)

    def move_to(self, x, y):
        self._kreis.move_to(x,y)

    # Geschwindigkeit basierend auf gedrückten Knöpfen ändern
    def change_speed(self):
        '''
        TODO: Dokumentation
        '''
        
        # aktuell gedrückte Taste
        pressed_key : str = self._raum.pressed_key()
        
        # wenn ich gerade w drücke 
        if pressed_key == "w":

            # dann setzt er die x-geschwindigkeit auf 0 und die y-Gewschwindigkeit auf -speed
            self.set_dx(0)
            self.set_dy(-1 * self._speed)
            
        # wenn ich gerade a drücke
        if pressed_key == "a":

            # dann setzt er die x-geschwindigkeit auf -speed und die y-Gewschwindigkeit auf 0
            self.set_dx(-1 * self._speed)
            self.set_dy(0)
    
        # wenn ich gerade s drücke
        if pressed_key == "s":
    
            # dann setzt er die x-Geschwindigkeit auf 0 und die y-Geschwindigkeit auf speed
            self.set_dx(0)
            self.set_dy(self._speed)
    
        # wenn ich gerade d drücke 
        if pressed_key == "d":
    
            # dann setzt er die x-Geschwindigkeit auf speed und die y-Geschwindigkeit auf 0
            self.set_dx(self._speed)
            self.set_dy(0)
    
        # wenn ich gerade q drücke 
        if pressed_key == "q":
    
            # dann setzt er die x-Geschwindigkeit auf minus die Wurzel von speed²/2 und die y-Geschwindigkeit auf minus die Wurzel von speed²/2
            self.set_dx(-1 * math.sqrt((self._speed * self._speed) / 2))
            self.set_dy(-1 * math.sqrt((self._speed * self._speed) / 2))
        
        # wenn ich gerade e drücke
        if pressed_key == "e":
    
            # dann setzt er die x-Geschwindigkeit auf die Wurzel von speed²/2 und die y-Geschwindigkeit auf minus die Wurzel von speed²/2
            self.set_dx(math.sqrt((self._speed * self._speed) / 2))
            self.set_dy(-1 * math.sqrt((self._speed * self._speed) / 2))
    
        # wenn ich gerade y drücke
        if pressed_key == "y":

            # dann setzt er die x-Geschwindigkeit auf minus die Wurzel von speed²/2 und die y-Geschwindigkeit auf die Wurzel von speed²/2
            self.set_dx(-1 * math.sqrt((self._speed * self._speed) / 2))
            self.set_dy(math.sqrt((self._speed * self._speed) / 2))
    
        # wenn ich gerade c drücke 
        if pressed_key == "c":
    
            # dann setzt er die x-Geschwindigkeit auf die Wurzel von speed²/2 und die y-Geschwindigkeit auf die Wurzel von speed²/2
            self.set_dx(math.sqrt((self._speed * self._speed) / 2))
            self.set_dy(math.sqrt((self._speed * self._speed) / 2))
    
        # wenn ich gerade nichts drücke
        if pressed_key == "":
    
            # dann soll er beides auf 0 setzen
            self.set_dx(0)
            self.set_dy(0)
        
    # auf Kollision überprüfen
    def check_wall_collision(self, current_room, l : int) -> None :
        '''
        TODO: Funktion schreiben, Dokumentation
        '''
        map_length = l

        # Höhe und Breite in Feldern (nicht Pixeln)
        room_height = current_room.get_height()
        room_length = current_room.get_length()

        layout = current_room.get_layout()

        # Größe der Felder nochmal berechnet (genau so wie bei der Map Klasse, 
        # aber natürlich ist es so nicht synchronisiert also wenn sich das bei Map ändert kann es zu 
        # Fehlern mit der collision kommen weil es hier so bleibt)
        tile_height = map_length // room_height
        tile_length = map_length // room_length

        x = self._kreis.get_x()
        y = self._kreis.get_y()

        dx = self.get_dx()
        dy = self.get_dy()

        radius = self._kreis.get_radius()
        offset = math.sqrt(radius**2/2)

        # Koordinaten wo ich beim nächsten Schritt wäre
        next_x = x + dx
        next_y = y + dy

        # berechnen, was die Koordinaten des Felds, wo ich lande, wenn der Spieler sich das nächste mal bewegt hat, sind
        next_tile_column : int = int(next_x / tile_length)
        next_tile_row : int = int(next_y / tile_height)

        # Punkte wo ich gucke ob sie beim nächsten Schritt in einer Wand wären, setzen sich aus 5 verschiedenen x- und 5 verschiedenen y-Koordinaten zusammen (für x links, die "Ecken" des Kreises oben links und unten links, mitte, die Ecken rechts und rechts. Für y oben, die Ecken oben links und oben rechts, mitte, die Ecken unten links und unten rechts und unten.) 
        
        test_points = [
            (next_x, next_y - radius), (next_x, next_y + radius), # Top, Bottom
            (next_x - radius, next_y), (next_x + radius, next_y), # Left, Right
            (next_x - offset, next_y - offset), (next_x + offset, next_y - offset), # Diagonale oben
            (next_x - offset, next_y + offset), (next_x + offset, next_y + offset)  # Diagonale unten
        ]

        for a, b in test_points:
            next_tile_column : int = int(a / tile_length)
            next_tile_row : int = int(b / tile_height)
            
            if layout[next_tile_row][next_tile_column] == 1:
                self.set_dx(0)
                self.set_dy(0)

            # Optional: dann, wenn es noch etwas zu bewegen gibt, gib 1 aus,

            # sonst, wenn ich genau dran wäre, gib 2 aus,
    
            # sonst, wenn nein, gib 0 aus
            # so könnte man steuern, dass er bis Anschlag zur Wand geht

    def attack(self, jetzt, gegner):

        delta = jetzt - self._last_attack_time
        
        pressed_key : str = self._raum.pressed_key()
        # wenn space gedrückt wird und die letzte Attacke nicht länger als der cooldown her ist

        if pressed_key == " " and delta > self._cooldown:

            self.set_last_attack_time(jetzt)
            
            x = self.get_x()
            y = self.get_y()
            attack_radius = self.get_radius() * self._attack_radius_ratio

            # Area of Effect der Attacke
            
            self.attack_circle.set_fill_rgb(255,0,0,0.5)

            for i in gegner:
                dx = x - i.get_x()
                dy = y - i.get_y()

                dist = math.sqrt(dx*dx + dy*dy)
    
                if dist <= attack_radius + i.get_radius():
                    i.lose_life(50)

            # player vor den Attack-Circle schieben
            self.to_front()

    
    def is_hit(self, jetzt, n):
        if jetzt - self._last_hit >= self._hit_cooldown:
            self._last_hit = jetzt
            self.lose_hp(50)
        


        

