import sys

sys.path.append('/usr/lib/otb/python')

import otbApplication 

def create_model(in_file, statistics_file, training_poly, output_model, confusion_matrix):
    """Creates a model which can be used as input for the classification function.
    Args:
        in_file (str): The file containing the tif image
        statistics_file (str): The output file to which the second order statistics will be written
        training_poly (str): Shape file (polygon) with known classes
    Result:
        A model on which the classification can be based.
    """
    #Create second order statistics application
    ComputeImagesStatistics = otbApplication.Registry.CreateApplication("ComputeImagesStatistics")
    #Set parameters for application
    ComputeImagesStatistics.SetParameterStringList("il", [in_file]) 
    ComputeImagesStatistics.SetParameterString("out", statistics_file)
    #Run application
    ComputeImagesStatistics.ExecuteAndWriteOutput()
    
    #Create train image classifier application
    TrainImagesClassifier = otbApplication.Registry.CreateApplication("TrainImagesClassifier")
    #Set parameters for application
    TrainImagesClassifier.SetParameterStringList("io.il", [in_file]) 
    TrainImagesClassifier.SetParameterStringList("io.vd", [training_poly]) 
    TrainImagesClassifier.SetParameterString("io.imstat", statistics_file) 
    TrainImagesClassifier.SetParameterInt("sample.mv", 1000) 
    TrainImagesClassifier.SetParameterInt("sample.mt", 1000) 
    TrainImagesClassifier.SetParameterFloat("sample.vtr", 0.5) 
    TrainImagesClassifier.SetParameterString("sample.edg","1") 
    TrainImagesClassifier.SetParameterString("sample.vfn", "id") 
    TrainImagesClassifier.SetParameterString("classifier","libsvm") 
    TrainImagesClassifier.SetParameterString("classifier.libsvm.k","linear")     
    TrainImagesClassifier.SetParameterFloat("classifier.libsvm.c", 1)     
    TrainImagesClassifier.SetParameterString("io.out", output_model)      
    TrainImagesClassifier.SetParameterString("io.confmatout", confusion_matrix)
    #Run application     
    TrainImagesClassifier.ExecuteAndWriteOutput()