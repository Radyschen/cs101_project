from algoviz.svg import SVGView, Circle, Rect, Text, Image
from random import randrange
import random

class Map:

    def __init__(self, length, height):
        self.layout = [[1 for col in range(height)] for row in range(length)] 
        self.height = height  # arrayhöhe
        self.length = length  # arraybreite
        self.walls = []
        

    def get_length(self):
        return self.length

    def get_height(self):
        return self.height

    def get_layout(self):
        return self.layout

    
    def set_length(self, length):
        self.length = length

    def set_height(self, height):
        self.height = height
        
    def set_layout(self, layout):
        self.layout = layout
    
    def create_maze(self, gegneranzahl):
        # random punkte
        ax = []
        ay = []
        for i in range(self.length*2):
            ax.append(random.randint(1,self.length - 2))
            ay.append(random.randint(1,self.length - 2))

        # verbinden der random punkte durch tunnel
        while len(ax) >= 2:
            self.create_tunnel(ax[0], ay[0], ax[1], ay[1])
            for i in range (2):
                ax.pop(0)
                ay.pop(0)



        # mitte frei
        mx = self.get_height() // 2
        my = self.get_length() // 2

        self.layout[mx][my] = 0
        self.layout[mx+1][my] = 0
        self.layout[mx][my+1] = 0
        self.layout[mx+1][my+1] = 0


        # gegnerfelder
        self.add_gegner(gegneranzahl, mx, my)

    
    def create_tunnel(self, x1, y1, x2, y2):
        self.layout[x1][y1] = 0
        
        while x1 != x2:
            if x1 < x2:
                x1 += 1
                self.layout[x1][y1] = 0
            else:
                x1 -= 1
                self.layout[x1][y1] = 0
                
        while y1 != y2:
            if y1 < y2:
                y1 += 1
                self.layout[x1][y1] = 0
            else:
                y1 -= 1
                self.layout[x1][y1] = 0

    
    def add_gegner(self, gegneranzahl, mx, my):
        while gegneranzahl > 0:
            x = random.randint(1,self.length - 1)
            y = random.randint(1,self.length - 1)

            if (self.layout[x][y] == 0) and ((x != mx) and (x != mx +1)) and ((y != my) and (y != my+1)):
                self.layout[x][y] = 2
                gegneranzahl -= 1
            


    
    def create_lobby(self):
        self.layout =  [
            [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 1, 1, 0, 1, 0, 1],
            [1, 0, 1, 0, 0, 1, 0, 1],
            [1, 0, 0, 0, 0, 1, 0, 1],
            [1, 0, 0, 0, 0, 1, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1],
        ]

        
    def create_end(self):
        self.layout =[
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1],
            [1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1],
            [1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1],
            [1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1],
            [1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        ]


        
    def zeichnen(self, view, l):
        
        w = l // self.length        #pixelbreite der wände
        h = l // self.height        #pixelhöhe der wände
        
        for i in range(self.length):
            for j in range(self.height):
                if self.layout[j][i] == 1:
                    #rect = Rect(i*w, j*h, w, h, view)
                    #rect.set_fill("grey")
                    #rect.set_stroke_width(3)
                    wall = Image("Wall.png", i*w, j*h, w, h, view)
                    self.walls.append(wall)
                if self.layout[j][i] == 2:
                    rect = Rect(i*w, j*h, w, h, view)
                    rect.set_fill_rgb( 255, 0, 0, 0.5)
                    rect.set_stroke_width(1)
                
