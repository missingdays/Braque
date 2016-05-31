
def get_color_diff_fitness(original_image, color_diff, power=2):

    def color_diff_fitness(image):
        
        diff = 0

        for x in range(len(image)):
            for y in range(len(image[0])):
                diff += color_diff(original_image[x][y] - image[x][y])**power;

        # Diff can be very big number so just (1/sqrt(diff)) would give very small results
        # 1e9 seems big enough
        return 1e9 / (diff**(1/power))

    return original_diff_fitness
