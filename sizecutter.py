import os

def cut_size(input_image, xoff, yoff, xsize, ysize, output_image):
    """Cuts the input image to the selected size
    Args:
        input_image (str): The image that should be cut
        xoff (int): The starting X pixel
        yoff (int): The starting y pixel
        xsize (int): The wanted x size of the image
        ysize (int): The wanted y size of the image
        output_image (str): The location of the output
    Result:
        A cut out of the input image
    """
    cmd = "gdal_translate -srcwin "+str(xoff)+" "+str(yoff)+" "+str(xsize)+" "+str(ysize)+" " + input_image + " " + output_image
    os.system(cmd)