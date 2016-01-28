import sys

sys.path.append('/usr/lib/otb/python')

import otbApplication 

def select_object(in_file, expression, min_size, OBIA, out_file):
    """Selects the defined objects from an input tif file.
    Args:
        in_file (str): The tif file containing the image
        expression (str): Expression to define the properties of the wanted selection
        min_size (int): The minimun size of the selection
        OBIA (str): The expression to define the shape of the selection
        out_file (str): File containing the output (shape or kml)
    Result:
        Shape or kml file containing the shapes of the selected objects
    """
    #Create connected component segmentation application
    ConnectedComponentSegmentation = otbApplication.Registry.CreateApplication("ConnectedComponentSegmentation") 
    #Set parameters for application
    ConnectedComponentSegmentation.SetParameterString("in", in_file)      
    ConnectedComponentSegmentation.SetParameterString("expr", expression)      
    ConnectedComponentSegmentation.SetParameterInt("minsize", min_size)      
    ConnectedComponentSegmentation.SetParameterString("obia", OBIA) 
    ConnectedComponentSegmentation.SetParameterString("out", out_file) 
    #Run application
    ConnectedComponentSegmentation.ExecuteAndWriteOutput()