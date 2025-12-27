from algoviz.svg import SVGView, Circle, Rect, Text

class Map:

    def __init__(self, length, height):
        self.layout = [[0 for col in range(height)] for row in range(length)] 
        self.height = height  # arrayhöhe
        self.length = length  # arraybreite
        self.walls = []
        
    def create_maze(self):
        for i in range(self.length):
            self.layout[i][1] = 1
        
    def zeichnen(self, view, l):
        
        w = l // self.length        #pixelbreite der wände
        h = l // self.height        #pixelhöhe der wände
        
        for i in range(self.length):
            for j in range(self.height):
                if self.layout[i][j] == 1:
                    rect = Rect(i*w, j*h, w, h, view)
                    rect.set_fill("white")
                    rect.set_stroke_width(10)
                    self.walls.append(rect)
