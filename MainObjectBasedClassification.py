#Libraries
from selectimage import select_image
from sizecutter import cut_size
from objectbased import select_object

#Files
in_file_obj = "/home/user/FinalAssignment/output/InputMapObject.tif"
out_file_object = "/home/user/FinalAssignment/output/OutputMapObject.shp"
out_file_all = "/home/user/FinalAssignment/output/OutputMapObjectAll.shp"

#Data source
url = "https://api.planet.com/v0/scenes/ortho/"
key = "a9dcf4c4685f46d38ef914c1fcc4c31c"

#Coordinates of point
point_obj = (-118.4, 34.084)
map_type_obj = "visual"
crop_file_obj = "/home/user/FinalAssignment/Downloads/DownloadFileObject_"+map_type_obj+".tif"

#Download the image
try:
    select_image(url, key, point_obj, map_type_obj, crop_file_obj)
except:
    print "ERROR: No map available"

#Cut to size
cut_size(crop_file_obj, 1250, 1500, 750, 750, in_file_obj)

##Use object based selection
min_size = 5 
#Select all dark-green objects
expression = "(p1b2 < 100) and ((p1b2 > p1b1)or(p1b2>p1b3)) and (p1b1 < 90) and (p1b3<90)"
#Select all objects
OBIA_none = ''
select_object(in_file_obj, expression, min_size, OBIA_none, out_file_all)
#Select all round objects
OBIA = "SHAPE_RegionRatio > 0.65"
select_object(in_file_obj, expression, min_size, OBIA, out_file_object)