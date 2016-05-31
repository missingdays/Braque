
__all__ = ["independent_mutation"]

def independent_mutation(image_gen, mutation_probability):

    for figure in image_gen.figures:
        if random.random() < mutation_probability:
            figure.mutate()
