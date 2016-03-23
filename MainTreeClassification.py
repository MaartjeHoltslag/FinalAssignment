############# First create the output and Downloads folder in                         #############
############# the FinalAssignment directory (or change directories to own preference) #############

# Stofzuigerzaag
# Jorn Habes & Maartje Holtslag
# 28-1-2016

#Libraries
from selectimage import select_image
from modelcreator import create_model
from classification import classify
from treeselection import select_trees
from sizecutter import cut_size
from greenpercentage import greencalculator

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
key = #Add own key

#Coordinates of point
point = (-122.486, 37.698)

#Set map type and file location
map_type = "visual"
crop_file = "/home/user/FinalAssignment/Downloads/DownloadFile_"+map_type+".tif"

#Download the image
try:
    select_image(url, key, point, map_type, crop_file)
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

#Calculate percentage green per quadrant (format: nw, sw, ne, se)
print greencalculator(output_map)

##Apply model to other map

#Files
output_map1 = "/home/user/FinalAssignment/output/ClassifiedImage1.tif"
selection_map1 = "/home/user/FinalAssignment/output/ClassifiedImageTrees1.tif"
in_file1 = "/home/user/FinalAssignment/output/InputMap1.tif"

#Coordinates of point
point1 = (-122.363, 37.707)

#Set map type and file location
map_type1 = "visual"
crop_file1 = "/home/user/FinalAssignment/Downloads/DownloadFile1_"+map_type1+".tif"

#Download the image
try:
    select_image(url, key, point1, map_type1, crop_file1)
except:
    print "ERROR: No map available"

#Cut to size
cut_size(crop_file1, 1500, 1000, 1500, 2000, in_file1)

#Apply model to other map
classify(output_model, in_file1, statistics_file, output_map1)

#Delete all none trees from dataset
select_trees(output_map1, selection_map1)

#Calculate percentage green per quadrant (format: nw, sw, ne, se)
print greencalculator(output_map1)
