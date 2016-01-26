from download import download_image
from modelcreator import create_model
from classification import classify
import sys
import os
import Image
import numpy

#sys.path.append('/usr/lib/otb/python')
#ITK_AUTOLOAD_PATH="/usr/local/lib/otb/applications"
#PYTHONPATH = "/usr/local/lib/otb/python"

import otbApplication 

#files
statistics_file = "/home/user/project/output/Statistics.xml"
in_file = "/home/user/project/20151107_200759_0b0a_analytic.tif"
confusion_matrix = "/home/user/project/output/Confusion.csv"
output_model = "/home/user/project/output/Output.model"
training_poly = "/home/user/project/TrainPoly.shp"
output_map = "/home/user/project/output/ClassifiedImage.tif"

#url = "https://api.planet.com/v0/scenes/ortho/"
#key = "a9dcf4c4685f46d38ef914c1fcc4c31c"
#
#sf_nw = (-122.486, 37.698)
#sf_se = (-122.487, 37.699)
#sf_ne = (sf_se[0], sf_nw[1])
#sf_sw = (sf_nw[0], sf_se[1])
#
#
#import geojson
#
#poly = geojson.Polygon([[sf_nw, sf_ne, sf_se, sf_sw, sf_nw]])
#intersects = geojson.dumps(poly)
#
#params = {
#    "intersects": intersects,
#}
# 
#r = requests.get(url, params=params, auth=(key, ''))
#r.raise_for_status()
#data = r.json()
#scenes_data = data["features"]
#   
#for scene in scenes_data:
#    thumb_link = scene["properties"]["data"]["products"]["analytic"]["full"]
#    download_image(thumb_link, key)

#Classifying map

#Creating model
create_model(in_file, statistics_file, training_poly, output_model, confusion_matrix)


#Apply model
classify(output_model, in_file, statistics_file, output_map)


image =Image.open(output_map)
array = numpy.array(image)



array2 = numpy.delete(array, [0])
testImage = Image.fromarray(array2)
testImage.save("/home/user/project/output/TestImage.tif")
print array



numpy.clip(array, 1,1,out=a)
for line in array:
    length_line = len(line)
    
    

for line in range(len(array)):
    for element in range(length_line):
        if array[line][element] != 1:
            array[line][element] = None
        else:
            array[line][element] = 1

#Display result


from osgeo import gdal, ogr
import sys
# this allows GDAL to throw Python Exceptions
gdal.UseExceptions()

#
#  get raster datasource
#
src_ds = gdal.Open(output_map)

try:
    srcband = src_ds.GetRasterBand(0)
except RuntimeError, e:
    # for example, try GetRasterBand(10)
    print 'Band ( %i ) not found' % band_num
    print e
    sys.exit(1)

#
#  create output datasource
#
dst_layername = "POLYGONIZED_STUFF"
drv = ogr.GetDriverByName("ESRI Shapefile")
dst_ds = drv.CreateDataSource( dst_layername + ".shp" )
dst_layer = dst_ds.CreateLayer(dst_layername, srs = None )

gdal.Polygonize( srcband, None, dst_layer, -1, [], callback=None )