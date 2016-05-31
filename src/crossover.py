
import random

__all__ = ["binary_crossover"]

def binary_crossover(image_1, image_2):

    new_image = image_1.copy()

    for i, figure in enumerate(image_2.figures):
        if random.random() < 0.5:
            new_image.figures[i] = figure.copy()

    return new_image
