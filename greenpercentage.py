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
    nw, sw, ne, se = array[:(lst[0]/2), :(lst[1]/2)], array[(lst[0]/2):, :(lst[1]/2)], array[:(lst[0]/2), (lst[1]/2):], array[(lst[0]/2):, (lst[1]/2):]
    for i in (nw, sw, ne, se):
        percentage = (100*float(numpy.sum(i)))/(count/4)
        print "The percentage of green for the {a:s} quadrant is {p:8.2f}".format(a=i, p=percentage)