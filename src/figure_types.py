
import random

class Figure:

    def __init__(self, coords=(0, 0), radius=0, alpha=0, color=(0, 0, 0)):
        self.x, self.y = coords
        
        self.radius = radius
        self.alpha = alpha

        self.color = color

    def copy(self):
        return Figure(self.coords, self.radius, self.alpha, self.color)

    def mutate(self):
        """
        Mutate will move figure, change its radius, alpha and color at random.
        This seems like very strong mutation, will consider changing it to something weaker.
        """

        self.x += random.randrange(-200, 200, 0.1)
        self.y += random.randrange(-200, 200, 0.1)
        self.radius += random.randrange(-self.radius, 50, 0.05)
        self.alpha = random.random()
        self.color = (random.randrange(256), random.randrange(256), random.randrange(256))

class Circle(Figure):

    def __init__(self, coords=(0, 0), radius=0, alpha=0, color=(0, 0, 0)):
        super().__init__(coords, radius, alpha, color)

    def draw(self, im):
        coords, radius, color = self.coords, self.radius, self.color

        draw = ImageDraw.Draw(im)
        draw.ellipse([coords[0]-radius, coords[1]-radius, coords[0]+radius, coords[1]+radius], color, color)

        del draw

class Square(Figure):

    def __init__(self, coords=(0, 0), radius=0, alpha=0, color=(0, 0, 0)):
        super().__init__(coords, radius, alpha, color)

    def draw(self, im):
        coords, radius, color = self.coords, self.radius, self.color

        draw = ImageDraw.Draw(im)
        draw.rectangle([coords[0]-radius, coords[1]-radius, coords[0]+radius, coords[1]+radius], color, color)

        del draw
