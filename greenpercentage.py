import Image
import numpy

def greencalculator(input_map):
    """Calculates the percentage of trees (green) of the input map.
    Args:
        input_map (str): The map from which the percentage of trees should be calculated
    Result:
        The percentage of green in the input map
    """
    image =Image.open(input_map)
    array = numpy.array(image)
    lst = array.shape
    count = lst[0]*lst[1]
    quadrants = array[:(lst[0]/2), :(lst[1]/2)], array[(lst[0]/2):, :(lst[1]/2)], array[:(lst[0]/2), (lst[1]/2):], array[(lst[0]/2):, (lst[1]/2):]
    green_list = []
    for i in quadrants:
        percentage = (100*float(numpy.sum(i)))/(count/4)
        green_list += [round(percentage, 3)]
    return green_list
        