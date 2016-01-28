#Libraries
from selectimage import select_image
from modelcreator import create_model
from classification import classify
from treeselection import select_trees
from sizecutter import cut_size

#Files
statistics_file = "/home/user/FinalAssignment/output/Statistics.xml"
confusion_matrix = "/home/user/FinalAssignment/output/Confusion.csv"
output_model = "/home/user/FinalAssignment/output/Output.model"
training_poly = "/home/user/FinalAssignment/TrainPolygon/TrainPoly.shp"
output_map = "/home/user/FinalAssignment/output/ClassifiedImage.tif"
selection_map = "/home/user/FinalAssignment/output/ClassifiedImageTrees.tif"
in_file = "/home/user/FinalAssignment/output/InputMap.tif"

#Data source
url = "https://api.planet.com/v0/scenes/ortho/"
key = "a9dcf4c4685f46d38ef914c1fcc4c31c"

#Coordinates of point
nw = (-122.486, 37.698)
se = (-122.487, 37.699)
map_type = "visual"
crop_file = "/home/user/FinalAssignment/DownloadFile_"+map_type+".tif"

#Download the image
try:
    select_image(url, key, nw, se, map_type, crop_file)
except:
    print "ERROR: No map available"

#Cut to size
cut_size(crop_file, 1500, 1000, 1500, 2000, in_file)

#Creating model to classify trees
create_model(in_file, statistics_file, training_poly, output_model, confusion_matrix)

#Apply model
classify(output_model, in_file, statistics_file, output_map)

#Delete all none trees from dataset
select_trees(output_map, selection_map)

##Apply model to other map

#Files
output_map1 = "/home/user/FinalAssignment/output/ClassifiedImage1.tif"
selection_map1 = "/home/user/FinalAssignment/output/ClassifiedImageTrees1.tif"
in_file1 = "/home/user/FinalAssignment/output/InputMap1.tif"

#Coordinates of point
nw1 = (-122.363, 37.707)
se1 = (-122.364, 37.708)
map_type1 = "visual"
crop_file1 = "/home/user/FinalAssignment/DownloadFile1_"+map_type1+".tif"

#Download the image
try:
    select_image(url, key, nw1, se1, map_type1, crop_file1)
except:
    print "ERROR: No map available"

#Cut to size
cut_size(crop_file1, 1500, 1000, 1500, 2000, in_file1)

#Apply model to other map
classify(output_model, in_file1, statistics_file, output_map1)

#Delete all none trees from dataset
select_trees(output_map1, selection_map1)