"""import rasterio as rs
import matplotlib as plt
from rasterio.plot import show
import georaster
import scipy
import osgeo

fp = r'data/climateEngine_SHumidity_CA_1980-82.sph.tif'
img = rs.open(fp)
#print (img.count) # number of bands
#print (img.height, img.width)
#print (img.crs) #coordinate referance system
#show(img)

#Below is the code for visualizing the image having more than one band (or channels).
img = georaster.SingleBandRaster('data/climateEngine_SHumidity_CA_1980-82.sph.tif')

# img.r gives the raster in [height, width, band] format 
# band no. starts from 0
plt.imshow(img.r[:,:,2]) """

import georaster
print(georaster.__file__)