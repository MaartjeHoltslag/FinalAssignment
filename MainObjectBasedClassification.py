#Libraries
from selectimage import select_image
from sizecutter import cut_size
from objectbased import select_object

#Files
in_file = "/home/user/FinalAssignment/output/InputMapObject.tif"
out_file = "/home/user/FinalAssignment/output/OutputMapObject.shp"

#Data source
url = "https://api.planet.com/v0/scenes/ortho/"
key = "a9dcf4c4685f46d38ef914c1fcc4c31c"

#Coordinates of point
#nw = (-118.4, 34.084)
#se = (-118.401, 34.085)
nw = (-118.184, 34.059)
se = (-118.185, 34.060)

#Download the image
try:
    select_image(url, key, nw, se, "visual")
except:
    print "ERROR: No map available"
#Load the downloaded image to a variable
crop_file = "/home/user/FinalAssignment/20150813_225645_0b09_visual.tif"

#Cut to size
cut_size(crop_file, 1250, 1500, 750, 750, in_file)

#Use object based selection for 
expression = "(p1b2 < 100) and ((p1b2 > p1b1)or(p1b2>p1b3)) and (p1b1 < 90) and (p1b3<90)"
min_size = 5 
OBIA = "SHAPE_RegionRatio > 0.65"

select_object(in_file, expression, min_size, OBIA, out_file)