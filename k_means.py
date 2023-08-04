# Jake Langenfeld

from math import *
from image_utils import *

def k_means(image, k):
    """
    Runs the k_means algorithm on an image. Takes an initial average color list and makes an initial
    assignments list. Then takes the assignments list and updates the means list. This runs until the
    assignments don't change anymore
    :param image: The image data, should be a width x height list-of-lists with each element
                being a 3-tuple of red,green,blue values each of which should be between 0 and 255.
    :param k: The number of colors for the new image
    :return: The means list with average k number of colors and 2d assignments list with each element
             representing a pixel and its assignment to its average color
    """
    means = initial_means(k)
    new_assignments = update_assignments(image, means)
    old_assignments = []
    width, height = get_width_height(image)

    while old_assignments != new_assignments:
        means = update_means(image, new_assignments, k)
        old_assignments = []
        for x in range(width):
            r = [0] * height
            old_assignments.append(r)
            for y in range(height):
                old_assignments[x][y] = new_assignments[x][y]
        new_assignments = update_assignments(image, means)

    return means, new_assignments


def distance(c1, c2):
    """
    Compares 2 colors and finds the "distance" between them. The lower the value the closer the colors are alike.
    :param c1: Color1, a 3-tuple consisting of red, green, and blue values ranging 0 to 255
    :param c2: Color2, a 3-tuple consisting of red, green, and blue values ranging 0 to 255
    :return: The "distance" between the colors.
    """
    r1, g1, b1 = c1
    r2, g2, b2 = c2
    red = pow((r1 - r2), 2)
    green = pow((g1 - g2), 2)
    blue = pow((b1 - b2), 2)
    
    return sqrt(red + green + blue)


def initial_means(k):
    """
    Creates a k length list filled with random colors
    :param k: Number of colors for new image
    :return: A list of k length filled with random colors
    """
    means = []
    for i in range(k):
        means.append(random_color())

    return means


def update_assignments(image, means):
    """
    Creates a new 2d list that represents the image and assigns each pixel to the index of closest average
    color in list means
    :param image: The image data, should be a width x height list-of-lists with each element
                being a 3-tuple of red,green,blue values each of which should be between 0 and 255.
    :param means: A list of average colors for the image
    :return: A 2d list of indexes referring to the average color from the means list
    """
    width, height = get_width_height(image)
    assignments = []

    for x in range(width):
        r = [0] * height
        assignments.append(r)
        for y in range(height):
            color_list = []
            for i in range(len(means)):
                color_list.append(distance(image[x][y], means[i]))
            assignments[x][y] = color_list.index(min(color_list))

    return assignments


def update_means(image, assignments, k):
    """
    Updates the average colors in the means list. Goes through the assignments list and takes the average
    color of all the pixels with the same index reference.
    :param image: The image data, should be a width x height list-of-lists with each element
                being a 3-tuple of red,green,blue values each of which should be between 0 and 255.
    :param assignments: A 2d list of indexes referring to the average color from the means list
    :param k: The number of colors for the new image
    :return: An updated list of the average colors
    """
    width, height = get_width_height(image)
    means = []
    assigned_colors = []

    for i in range(k):
        for x in range(width):
            for y in range(height):
                if assignments[x][y] == i:
                    assigned_colors.append(image[x][y])
        means.append(average_color(assigned_colors))

    return means


def average_color(color_list):
    """
    Finds the average color of all the pixels that are associated with the same average color from the means list
    :param color_list: List of indexes that refer to the same average color
    :return: Average value for each color value
    """
    if len(color_list) == 0:
        return 0, 0, 0
    red = 0
    green = 0
    blue = 0
    for i in range(len(color_list)):
        r, g, b = color_list[i]
        red += r
        green += g
        blue += b

    return int(red / len(color_list)), int(green / len(color_list)), int(blue / len(color_list))

