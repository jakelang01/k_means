# Jake Langenfeld

from k_means import *
from image_utils import *

def run_k_means():
    """
    Runs the k_means algorithm to change the colors of the given .ppm image
    :return: An unmodified picture and modified picture based on k
    """
    file = input("Image file> ")
    k = int(input("Number of colors> "))
    filename_unmodified = input("Preferred name for unmodified file> ")
    filename_modified = input("Preferred name for modified file> ")
    
    image = read_ppm(file)
    save_ppm(filename_unmodified, image)

    means, assignments = k_means(image, k)
    for x in range(len(assignments)):
        for y in range(len(assignments[0])):
            for i in range(k):
                if assignments[x][y] == i:
                    image[x][y] = means[i]

    save_ppm(filename_modified, image)

if __name__=="__main__":
    run_k_means()