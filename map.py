from algoviz.svg import SVGView, Circle, Rect, Text

class Map:

    def __init__(self, length, height):
        self.layout = [[0 for col in range(height)] for row in range(length)] 
        self.height = height  # arrayhöhe
        self.length = length  # arraybreite
        self.walls = []
        self.create_maze()

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
    
    def create_maze(self):
        for i in range(self.length):
            self.layout[i][1] = 1

    def create_lobby(self):
        self.layout = [
            [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 1, 1, 0, 1, 0, 1],
            [1, 0, 0, 0, 0, 1, 0, 1],
            [1, 0, 0, 0, 0, 1, 0, 1],
            [1, 0, 0, 0, 0, 1, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1],
        ]

        
    def create_end(self):
        self.layout = [
            [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 1, 1, 1, 1, 0, 1],
            [1, 0, 1, 0, 0, 1, 0, 1],
            [1, 0, 1, 0, 0, 1, 0, 1],
            [1, 0, 1, 0, 0, 1, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1],
        ]


        
    def zeichnen(self, view, l):
        
        w = l // self.length        #pixelbreite der wände
        h = l // self.height        #pixelhöhe der wände
        
        for i in range(self.length):
            for j in range(self.height):
                if self.layout[j][i] == 1:
                    rect = Rect(i*w, j*h, w, h, view)
                    rect.set_fill("white")
                    rect.set_stroke_width(5)
                    self.walls.append(rect)
