from download import download_image
from modelcreator import create_model
from classification import classify
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

#url = "https://api.planet.com/v0/scenes/ortho/"
#key = "a9dcf4c4685f46d38ef914c1fcc4c31c"
#
#sf_nw = (-122.486, 37.698)
#sf_se = (-122.487, 37.699)
#sf_ne = (sf_se[0], sf_nw[1])
#sf_sw = (sf_nw[0], sf_se[1])
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
#


#original = Image.open(output_map)
#width, height = original.size
#left = width/4
#top = height/4
#right = 3 * (width/4)
#bottom = 3 * (height/4)
#crop_map = original.crop((left, top, right, bottom))
#crop_map.save("/home/user/FinalAssignment/output/ClassifiedCroppedImage.tif")

#Classifying map

#Creating model
create_model(in_file, statistics_file, training_poly, output_model, confusion_matrix)


#Apply model
classify(output_model, in_file, statistics_file, output_map)

#Delete all none trees from dataset
image =Image.open(output_map)
array = numpy.array(image)

#numpy.where(array==0,-9999,array)
dataSource = gdal.Open(output_map, GA_ReadOnly)

# Write the result to disk
driver = gdal.GetDriverByName('GTiff')
outDataSet=driver.Create('/home/user/FinalAssignment/output/ClassifiedImageArray.tif', dataSource.RasterXSize, dataSource.RasterYSize, 1, GDT_Float32)
outBand = outDataSet.GetRasterBand(1)
outBand.WriteArray(array,0,0)
outBand.SetNoDataValue(0)

# set the projection and extent information of the dataset
outDataSet.SetProjection(dataSource.GetProjection())
outDataSet.SetGeoTransform(dataSource.GetGeoTransform())

# Finally let's save it... or like in the OGR example flush it
outBand.FlushCache()
outDataSet.FlushCache()

#Set to kml file
dataset = gdal.Open(output_map, GA_ReadOnly)
cmd = "gdal2tiles.py -r near -k "+ output_map + " /home/user/FinalAssignment/output"
os.system(cmd)


original = Image.open('/home/user/FinalAssignment/output/ClassifiedImageArray.tif')
width, height = original.size
left = width/4
top = height/4
right = 3 * (width/4)
bottom = 3 * (height/4)
crop_map = original.crop((left, top, right, bottom))
crop_map.save("/home/user/FinalAssignment/output/ClassifiedCroppedImage.tif")
crop_image = "/home/user/FinalAssignment/output/ClassifiedCroppedImage.tif"


cmdo = "gdalwarp -t_srs 'EPSG:4326' "+ crop_image + " /home/user/FinalAssignment/output/ClassifiedCroppedImageLatLon.tif"
os.system(cmdo)