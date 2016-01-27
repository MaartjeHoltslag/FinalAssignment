from download import *
from modelcreator import create_model
from classification import classify
from treeselection import select_trees
import geojson
import sys
import os
import gdal
from gdalconst import *
from osgeo.gdalconst import GA_ReadOnly, GDT_Float32
from PIL import Image
import numpy
import otbApplication 

#files
statistics_file = "/home/user/FinalAssignment/output/Statistics.xml"
crop_file = "/home/user/FinalAssignment/20151107_200759_0b0a_analytic.tif"
confusion_matrix = "/home/user/FinalAssignment/output/Confusion.csv"
output_model = "/home/user/FinalAssignment/output/Output.model"
training_poly = "/home/user/FinalAssignment/TrainPoly.shp"
output_map = "/home/user/FinalAssignment/output/ClassifiedImage.tif"
selection_map = "/home/user/FinalAssignment/output/ClassifiedImageTrees.tif"
in_file = "/home/user/FinalAssignment/output/InputMap.tif"

url = "https://api.planet.com/v0/scenes/ortho/"
key = "a9dcf4c4685f46d38ef914c1fcc4c31c"

nw = (-122.486, 37.698)
se = (-122.487, 37.699)

#Download the image
select_image(url, key, nw, se)
#Cut to size
cmd1 = "gdal_translate -srcwin 1500 1000 1500 2000 " + crop_file + " " + in_file
os.system(cmd1)

#Creating model to classify trees
create_model(in_file, statistics_file, training_poly, output_model, confusion_matrix)

#Apply model
classify(output_model, in_file, statistics_file, output_map)

#Delete all none trees from dataset
select_trees(output_map, selection_map)

##Set to kml file
#dataset = gdal.Open("/home/user/FinalAssignment/output/ClassifiedImageArray.tif", GA_ReadOnly)
#cmd = "gdal2tiles.py -a -k /home/user/FinalAssignment/output/ClassifiedImageArray.tif /home/user/FinalAssignment/output"
#os.system(cmd)
