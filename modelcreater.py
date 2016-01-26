import sys

sys.path.append('/usr/lib/otb/python')

import otbApplication 

def create_model(in_file, statistics_file):
    """Creates a model which can be used as input for the classification function.
    Args:
        in_file (str): The file containing the tif image
        statistics_file (str): The output file to which the second order statistics will be written
    Result:
        A model on which the classification can be based.
    """
    ComputeImagesStatistics = otbApplication.Registry.CreateApplication("ComputeImagesStatistics") 
    ComputeImagesStatistics.SetParameterStringList("il", [in_file]) 
    ComputeImagesStatistics.SetParameterString("out", statistics_file) 
    ComputeImagesStatistics.ExecuteAndWriteOutput()
    