
import random

from figure_types import *

__all__ = ["ImageGenFabric"]

class ImageGenFabric:
    def __init__(self, figure_number=100, figure_types=[Circle, Square]):
        self.figure_number = figure_number

        if len(figure_types) == 0:
            raise Exception("Figure types list must contain atleast one figure type")
        self.figure_types = figure_types

    def new(self):
        return ImageGen(self.figure_number, figure_types)

    def random(self):
        image_gen = self.new()

        image_gen.randomize()

        return image_gen

class ImageGen:

    def __init__(self, figure_number, figure_types):
        self.figure_number = figure_number
        self.figures = [figure_types[0]() for i in figure_number]

    def copy(self):
        new_image = ImageGen(self.figure_number, self.figure_types)

        new_image.figures = []

        for figure in image.figures:
            new_image.figures.append(figure.copy())

        return new_image

    def randomize(self):

        for i in range(len(self.figures)):
            figure_type = random.choice(self.figure_types)

            self.figures[i] = figure_type()
            self.figures[i].randomize()
