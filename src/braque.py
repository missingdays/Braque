
import sys

from PIL import Image

from genetic_algorithm import GeneticAlgorithm

def draw(image_name, genetic_algorithm):

    image_pixels = Image.open(image_name).load()

    genetic_algorithm.set_original_image(image_pixels)

    for images, cycle in genetic_algorithm:
        
        if cycle % 100 == 0:
            best_image = images.get_best_image()

            best_image.save("{0}-{1}".fortmat(image_name, cycle))

if __name__ == "__main__":

    genetic_algorithm = GeneticAlgorithm()

    draw(sys.argv[1], genetic_algorithm)
