import gdal
from gdalconst import *
from osgeo.gdalconst import GA_ReadOnly, GDT_Float32

def select_trees(input_map, output_map):
    """Select the trees from the input map and set the rest to NoData
    Args:
        input_map (str): The tif file containing the defined classes
    Result:
        A tif file containing only the tree class
    """
    image =Image.open(input_map)
    array = numpy.array(image)
    dataSource = gdal.Open(input_map, GA_ReadOnly)
    driver = gdal.GetDriverByName('GTiff')
    outDataSet=driver.Create(output_map, dataSource.RasterXSize, dataSource.RasterYSize, 1, GDT_Float32)
    outBand = outDataSet.GetRasterBand(1)
    outBand.WriteArray(array,0,0)
    outBand.SetNoDataValue(0)
    outDataSet.SetProjection(dataSource.GetProjection())
    outDataSet.SetGeoTransform(dataSource.GetGeoTransform())
    outBand.FlushCache()
    outDataSet.FlushCache()