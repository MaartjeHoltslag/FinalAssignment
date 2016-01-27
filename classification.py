import sys

sys.path.append('/usr/lib/otb/python')

import otbApplication 

def classify(input_model, in_file, statistics_file, output_map):
    """Classifies a map using an input training model
    Args:
        input_model (str): The input training model
        in_file (str): The file containing the tif image
        statistics_file (str): The file in which the second order statistics is written
        output_map (str): A tif file containing the classified map
    Result:
        Tif file containing a classified map.
    """
    #Create image classifier application
    ImageClassifier = otbApplication.Registry.CreateApplication("ImageClassifier")
    #Set parameters for application
    ImageClassifier.SetParameterString("in", in_file)      
    ImageClassifier.SetParameterString("imstat", statistics_file)      
    ImageClassifier.SetParameterString("model", input_model)      
    ImageClassifier.SetParameterString("out", output_map)
    #Run application      
    ImageClassifier.ExecuteAndWriteOutput()