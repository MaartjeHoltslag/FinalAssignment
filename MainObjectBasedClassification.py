#Libraries
from selectimage import select_image


#Files
crop_file = "/home/user/FinalAssignment/20150813_225645_0b09_visual.tif"
in_file = "/home/user/FinalAssignment/output/InputMapObject.tif"

#Data source
url = "https://api.planet.com/v0/scenes/ortho/"
key = "a9dcf4c4685f46d38ef914c1fcc4c31c"

#Coordinates of point
nw = (-118.4, 34.084)
se = (-118.401, 34.085)

#Download the image
select_image(url, key, nw, se)

#Cut to size
cmd1 = "gdal_translate -srcwin 1250 1500 750 750 " + crop_file + " " + in_file
os.system(cmd1)

